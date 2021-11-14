# Copyright 2020 Adap GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Flower server tests."""


import time
from typing import List, Sequence, Tuple, Union

import numpy as np

from flwr.common import (
    Disconnect,
    EvaluateIns,
    EvaluateRes,
    FitIns,
    FitRes,
    Parameters,
    ParametersRes,
    PropertiesIns,
    PropertiesRes,
    Reconnect,
    ndarray_to_bytes,
)

from .client_proxy import ClientProxy
from .server import evaluate_clients, execute_round, fit_client, fit_clients


class SleepingClientProxy(ClientProxy):
    """ClientProxy that blocks for exec_time seconds."""

    def __init__(self, cid: str, exec_time: float):
        super().__init__(cid)
        self.cid = cid
        self.exec_time = exec_time

    def get_properties(self, ins: PropertiesIns) -> PropertiesRes:
        raise Exception()

    def get_parameters(self) -> ParametersRes:
        # This method is not expected to be called
        raise Exception()

    def fit(self, ins: FitIns) -> FitRes:
        # Sleep to simulate client-side execution
        time.sleep(self.exec_time)

        # Return some result
        arr = np.array([[1, 2], [3, 4], [5, 6]])
        arr_serialized = ndarray_to_bytes(arr)
        return FitRes(Parameters(tensors=[arr_serialized], tensor_type=""), 1, 1, 12.3)

    def evaluate(self, ins: EvaluateIns) -> EvaluateRes:
        # This method is not expected to be called
        raise Exception()

    def reconnect(self, reconnect: Reconnect) -> Disconnect:
        raise Exception()


class SuccessClient(ClientProxy):
    """Test class."""

    def get_parameters(self) -> ParametersRes:
        # This method is not expected to be called
        raise Exception()

    def get_properties(self, ins: PropertiesIns) -> PropertiesRes:
        raise Exception()

    def fit(self, ins: FitIns) -> FitRes:
        arr = np.array([[1, 2], [3, 4], [5, 6]])
        arr_serialized = ndarray_to_bytes(arr)
        return FitRes(Parameters(tensors=[arr_serialized], tensor_type=""), 1, 1, 12.3)

    def evaluate(self, ins: EvaluateIns) -> EvaluateRes:
        return EvaluateRes(loss=1.0, num_examples=1)

    def reconnect(self, reconnect: Reconnect) -> Disconnect:
        return Disconnect(reason="UNKNOWN")


class FailingCLient(ClientProxy):
    """Test class."""

    def get_parameters(self) -> ParametersRes:
        raise Exception()

    def get_properties(self, ins: PropertiesIns) -> PropertiesRes:
        raise Exception()

    def fit(self, ins: FitIns) -> FitRes:
        raise Exception()

    def evaluate(self, ins: EvaluateIns) -> EvaluateRes:
        raise Exception()

    def reconnect(self, reconnect: Reconnect) -> Disconnect:
        raise Exception()


def test_fit_clients() -> None:
    """Test fit_clients."""
    # Prepare
    clients: List[ClientProxy] = [
        FailingCLient("0"),
        SuccessClient("1"),
    ]
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    arr_serialized = ndarray_to_bytes(arr)
    ins: FitIns = FitIns(Parameters(tensors=[arr_serialized], tensor_type=""), {})
    client_instructions = [(c, ins) for c in clients]

    # Execute
    results, failures = fit_clients(client_instructions, None, None)

    # Assert
    assert len(results) == 1
    assert len(failures) == 1
    assert results[0][1].num_examples == 1


def test_eval_clients() -> None:
    """Test eval_clients."""
    # Prepare
    clients: List[ClientProxy] = [
        FailingCLient("0"),
        SuccessClient("1"),
    ]
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    arr_serialized = ndarray_to_bytes(arr)
    ins: EvaluateIns = EvaluateIns(
        Parameters(tensors=[arr_serialized], tensor_type=""),
        {},
    )
    client_instructions = [(c, ins) for c in clients]

    # Execute
    results, failures = evaluate_clients(client_instructions, None, None)

    # Assert
    assert len(results) == 1
    assert len(failures) == 1
    assert results[0][1].loss == 1.0
    assert results[0][1].num_examples == 1


def _create_client_instructions(
    exec_times: List[float],
) -> Sequence[Union[Tuple[ClientProxy, FitIns], Tuple[ClientProxy, EvaluateIns]]]:
    clients: List[ClientProxy] = [
        SleepingClientProxy(str(i), t) for i, t in enumerate(exec_times)
    ]
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    arr_serialized = ndarray_to_bytes(arr)
    ins: FitIns = FitIns(Parameters(tensors=[arr_serialized], tensor_type=""), {})
    # client_instructions: List[Tuple[ClientProxy, Union[FitIns, EvaluateIns]]] = [
    client_instructions = [(c, ins) for c in clients]
    return client_instructions


def test_execute_round_timeout_none() -> None:
    """."""
    # Prepare
    round_timeout = None
    exec_times = [0.1, 0.3, 0.2]
    client_instructions = _create_client_instructions(exec_times)

    # Execute
    finished_fs, unfinished_fs = execute_round(
        client_instructions,
        task_fn=fit_client,  # type: ignore
        max_workers=None,
        round_timeout=round_timeout,
    )

    # Assert
    assert len(finished_fs) == len(exec_times)
    assert len(unfinished_fs) == 0


def test_execute_round_timeout_high() -> None:
    """."""
    # Prepare
    round_timeout = 2
    exec_times = [1.1, 1.3, 1.2]
    client_instructions = _create_client_instructions(exec_times)

    # Execute
    finished_fs, unfinished_fs = execute_round(
        client_instructions,
        task_fn=fit_client,  # type: ignore
        max_workers=None,
        round_timeout=round_timeout,
    )

    # Assert
    assert len(finished_fs) == len(exec_times)
    assert len(unfinished_fs) == 0


def test_execute_round_timeout_some() -> None:
    """."""
    # Prepare
    round_timeout = 1.35
    exec_times = [1.1, 1.3, 1.2, 1.5, 1.4]
    client_instructions = _create_client_instructions(exec_times)

    # Execute
    finished_fs, unfinished_fs = execute_round(
        client_instructions,
        task_fn=fit_client,  # type: ignore
        max_workers=None,
        round_timeout=round_timeout,
    )

    # Assert
    assert len(finished_fs) == 3
    assert len(unfinished_fs) == 2


def test_execute_round_timeout_all() -> None:
    """."""
    # Prepare
    round_timeout = 0.5
    exec_times = [1.1, 1.3, 1.2, 1.5, 1.4]
    client_instructions = _create_client_instructions(exec_times)

    # Execute
    finished_fs, unfinished_fs = execute_round(
        client_instructions,
        task_fn=fit_client,  # type: ignore
        max_workers=None,
        round_timeout=round_timeout,
    )

    # Assert
    assert len(finished_fs) == 0
    assert len(unfinished_fs) == len(exec_times)
