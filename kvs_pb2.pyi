from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyRequest(_message.Message):
    __slots__ = ["key", "ver"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VER_FIELD_NUMBER: _ClassVar[int]
    key: str
    ver: int
    def __init__(self, key: _Optional[str] = ..., ver: _Optional[int] = ...) -> None: ...

class KeyRange(_message.Message):
    __slots__ = ["fr", "to"]
    FR_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    fr: KeyRequest
    to: KeyRequest
    def __init__(self, fr: _Optional[_Union[KeyRequest, _Mapping]] = ..., to: _Optional[_Union[KeyRequest, _Mapping]] = ...) -> None: ...

class KeyValueRequest(_message.Message):
    __slots__ = ["key", "val"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    key: str
    val: str
    def __init__(self, key: _Optional[str] = ..., val: _Optional[str] = ...) -> None: ...

class KeyValueVersionReply(_message.Message):
    __slots__ = ["key", "val", "ver"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    VER_FIELD_NUMBER: _ClassVar[int]
    key: str
    val: str
    ver: int
    def __init__(self, key: _Optional[str] = ..., val: _Optional[str] = ..., ver: _Optional[int] = ...) -> None: ...

class PutReply(_message.Message):
    __slots__ = ["key", "old_val", "old_ver", "ver"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OLD_VAL_FIELD_NUMBER: _ClassVar[int]
    OLD_VER_FIELD_NUMBER: _ClassVar[int]
    VER_FIELD_NUMBER: _ClassVar[int]
    key: str
    old_val: str
    old_ver: int
    ver: int
    def __init__(self, key: _Optional[str] = ..., old_val: _Optional[str] = ..., old_ver: _Optional[int] = ..., ver: _Optional[int] = ...) -> None: ...
