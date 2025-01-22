from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Endereco(_message.Message):
    __slots__ = ("numero",)
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    numero: str
    def __init__(self, numero: _Optional[str] = ...) -> None: ...

class Carta(_message.Message):
    __slots__ = ("texto",)
    TEXTO_FIELD_NUMBER: _ClassVar[int]
    texto: str
    def __init__(self, texto: _Optional[str] = ...) -> None: ...
