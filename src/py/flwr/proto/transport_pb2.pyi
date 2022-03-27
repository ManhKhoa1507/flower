"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Code:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _CodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Code.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _Code.ValueType  # 0
    GET_PARAMETERS_NOT_IMPLEMENTED: _Code.ValueType  # 1
class Code(_Code, metaclass=_CodeEnumTypeWrapper):
    pass

OK: Code.ValueType  # 0
GET_PARAMETERS_NOT_IMPLEMENTED: Code.ValueType  # 1
global___Code = Code


class _Reason:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Reason.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _Reason.ValueType  # 0
    RECONNECT: _Reason.ValueType  # 1
    POWER_DISCONNECTED: _Reason.ValueType  # 2
    WIFI_UNAVAILABLE: _Reason.ValueType  # 3
    ACK: _Reason.ValueType  # 4
class Reason(_Reason, metaclass=_ReasonEnumTypeWrapper):
    pass

UNKNOWN: Reason.ValueType  # 0
RECONNECT: Reason.ValueType  # 1
POWER_DISCONNECTED: Reason.ValueType  # 2
WIFI_UNAVAILABLE: Reason.ValueType  # 3
ACK: Reason.ValueType  # 4
global___Reason = Reason


class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: global___Code.ValueType
    message: typing.Text
    def __init__(self,
        *,
        code: global___Code.ValueType = ...,
        message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code",b"code","message",b"message"]) -> None: ...
global___Status = Status

class Parameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TENSORS_FIELD_NUMBER: builtins.int
    TENSOR_TYPE_FIELD_NUMBER: builtins.int
    @property
    def tensors(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    tensor_type: typing.Text
    def __init__(self,
        *,
        tensors: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        tensor_type: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tensor_type",b"tensor_type","tensors",b"tensors"]) -> None: ...
global___Parameters = Parameters

class ServerMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Reconnect(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        SECONDS_FIELD_NUMBER: builtins.int
        seconds: builtins.int
        def __init__(self,
            *,
            seconds: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["seconds",b"seconds"]) -> None: ...

    class GetParameters(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        def __init__(self,
            ) -> None: ...

    class FitIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        CONFIG_FIELD_NUMBER: builtins.int
        @property
        def parameters(self) -> global___Parameters: ...
        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            parameters: typing.Optional[global___Parameters] = ...,
            config: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config","parameters",b"parameters"]) -> None: ...

    class EvaluateIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        CONFIG_FIELD_NUMBER: builtins.int
        @property
        def parameters(self) -> global___Parameters: ...
        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            parameters: typing.Optional[global___Parameters] = ...,
            config: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config","parameters",b"parameters"]) -> None: ...

    class PropertiesIns(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ConfigEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        CONFIG_FIELD_NUMBER: builtins.int
        @property
        def config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            config: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["config",b"config"]) -> None: ...

    RECONNECT_FIELD_NUMBER: builtins.int
    GET_PARAMETERS_FIELD_NUMBER: builtins.int
    FIT_INS_FIELD_NUMBER: builtins.int
    EVALUATE_INS_FIELD_NUMBER: builtins.int
    PROPERTIES_INS_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    @property
    def reconnect(self) -> global___ServerMessage.Reconnect: ...
    @property
    def get_parameters(self) -> global___ServerMessage.GetParameters: ...
    @property
    def fit_ins(self) -> global___ServerMessage.FitIns: ...
    @property
    def evaluate_ins(self) -> global___ServerMessage.EvaluateIns: ...
    @property
    def properties_ins(self) -> global___ServerMessage.PropertiesIns: ...
    timeout: builtins.float
    """When the field is not explicitly set it will default to zero in gRPC
    therefore all implementations using it should treat 0 as no timeout
    """

    def __init__(self,
        *,
        reconnect: typing.Optional[global___ServerMessage.Reconnect] = ...,
        get_parameters: typing.Optional[global___ServerMessage.GetParameters] = ...,
        fit_ins: typing.Optional[global___ServerMessage.FitIns] = ...,
        evaluate_ins: typing.Optional[global___ServerMessage.EvaluateIns] = ...,
        properties_ins: typing.Optional[global___ServerMessage.PropertiesIns] = ...,
        timeout: builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["evaluate_ins",b"evaluate_ins","fit_ins",b"fit_ins","get_parameters",b"get_parameters","msg",b"msg","properties_ins",b"properties_ins","reconnect",b"reconnect"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["evaluate_ins",b"evaluate_ins","fit_ins",b"fit_ins","get_parameters",b"get_parameters","msg",b"msg","properties_ins",b"properties_ins","reconnect",b"reconnect","timeout",b"timeout"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["msg",b"msg"]) -> typing.Optional[typing_extensions.Literal["reconnect","get_parameters","fit_ins","evaluate_ins","properties_ins"]]: ...
global___ServerMessage = ServerMessage

class ClientMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Disconnect(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        REASON_FIELD_NUMBER: builtins.int
        reason: global___Reason.ValueType
        def __init__(self,
            *,
            reason: global___Reason.ValueType = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["reason",b"reason"]) -> None: ...

    class ParametersRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PARAMETERS_FIELD_NUMBER: builtins.int
        @property
        def parameters(self) -> global___Parameters: ...
        def __init__(self,
            *,
            parameters: typing.Optional[global___Parameters] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> None: ...

    class FitRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class MetricsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        PARAMETERS_FIELD_NUMBER: builtins.int
        NUM_EXAMPLES_FIELD_NUMBER: builtins.int
        METRICS_FIELD_NUMBER: builtins.int
        @property
        def parameters(self) -> global___Parameters: ...
        num_examples: builtins.int
        @property
        def metrics(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            parameters: typing.Optional[global___Parameters] = ...,
            num_examples: builtins.int = ...,
            metrics: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["metrics",b"metrics","num_examples",b"num_examples","parameters",b"parameters"]) -> None: ...

    class EvaluateRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class MetricsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        NUM_EXAMPLES_FIELD_NUMBER: builtins.int
        LOSS_FIELD_NUMBER: builtins.int
        METRICS_FIELD_NUMBER: builtins.int
        num_examples: builtins.int
        loss: builtins.float
        @property
        def metrics(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            num_examples: builtins.int = ...,
            loss: builtins.float = ...,
            metrics: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["loss",b"loss","metrics",b"metrics","num_examples",b"num_examples"]) -> None: ...

    class PropertiesRes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class PropertiesEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Scalar: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Scalar] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        STATUS_FIELD_NUMBER: builtins.int
        PROPERTIES_FIELD_NUMBER: builtins.int
        @property
        def status(self) -> global___Status: ...
        @property
        def properties(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Scalar]: ...
        def __init__(self,
            *,
            status: typing.Optional[global___Status] = ...,
            properties: typing.Optional[typing.Mapping[typing.Text, global___Scalar]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["status",b"status"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["properties",b"properties","status",b"status"]) -> None: ...

    DISCONNECT_FIELD_NUMBER: builtins.int
    PARAMETERS_RES_FIELD_NUMBER: builtins.int
    FIT_RES_FIELD_NUMBER: builtins.int
    EVALUATE_RES_FIELD_NUMBER: builtins.int
    PROPERTIES_RES_FIELD_NUMBER: builtins.int
    @property
    def disconnect(self) -> global___ClientMessage.Disconnect: ...
    @property
    def parameters_res(self) -> global___ClientMessage.ParametersRes: ...
    @property
    def fit_res(self) -> global___ClientMessage.FitRes: ...
    @property
    def evaluate_res(self) -> global___ClientMessage.EvaluateRes: ...
    @property
    def properties_res(self) -> global___ClientMessage.PropertiesRes: ...
    def __init__(self,
        *,
        disconnect: typing.Optional[global___ClientMessage.Disconnect] = ...,
        parameters_res: typing.Optional[global___ClientMessage.ParametersRes] = ...,
        fit_res: typing.Optional[global___ClientMessage.FitRes] = ...,
        evaluate_res: typing.Optional[global___ClientMessage.EvaluateRes] = ...,
        properties_res: typing.Optional[global___ClientMessage.PropertiesRes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disconnect",b"disconnect","evaluate_res",b"evaluate_res","fit_res",b"fit_res","msg",b"msg","parameters_res",b"parameters_res","properties_res",b"properties_res"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["disconnect",b"disconnect","evaluate_res",b"evaluate_res","fit_res",b"fit_res","msg",b"msg","parameters_res",b"parameters_res","properties_res",b"properties_res"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["msg",b"msg"]) -> typing.Optional[typing_extensions.Literal["disconnect","parameters_res","fit_res","evaluate_res","properties_res"]]: ...
global___ClientMessage = ClientMessage

class Scalar(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DOUBLE_FIELD_NUMBER: builtins.int
    SINT64_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    double: builtins.float
    sint64: builtins.int
    """float float = 2;
    int32 int32 = 3;
    int64 int64 = 4;
    uint32 uint32 = 5;
    uint64 uint64 = 6;
    sint32 sint32 = 7;
    """

    bool: builtins.bool
    """fixed32 fixed32 = 9;
    fixed64 fixed64 = 10;
    sfixed32 sfixed32 = 11;
    sfixed64 sfixed64 = 12;
    """

    string: typing.Text
    bytes: builtins.bytes
    def __init__(self,
        *,
        double: builtins.float = ...,
        sint64: builtins.int = ...,
        bool: builtins.bool = ...,
        string: typing.Text = ...,
        bytes: builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bool",b"bool","bytes",b"bytes","double",b"double","scalar",b"scalar","sint64",b"sint64","string",b"string"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bool",b"bool","bytes",b"bytes","double",b"double","scalar",b"scalar","sint64",b"sint64","string",b"string"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["scalar",b"scalar"]) -> typing.Optional[typing_extensions.Literal["double","sint64","bool","string","bytes"]]: ...
global___Scalar = Scalar
