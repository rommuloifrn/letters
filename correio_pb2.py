# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: correio.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'correio.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcorreio.proto\"\x1a\n\x08\x45ndereco\x12\x0e\n\x06numero\x18\x01 \x02(\t\"\x16\n\x05\x43\x61rta\x12\r\n\x05texto\x18\x01 \x02(\t2P\n\x07\x43orreio\x12\"\n\tGetCartas\x12\t.Endereco\x1a\x06.Carta\"\x00\x30\x01\x12!\n\nSendCartas\x12\x06.Carta\x1a\t.Endereco\"\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'correio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENDERECO']._serialized_start=17
  _globals['_ENDERECO']._serialized_end=43
  _globals['_CARTA']._serialized_start=45
  _globals['_CARTA']._serialized_end=67
  _globals['_CORREIO']._serialized_start=69
  _globals['_CORREIO']._serialized_end=149
# @@protoc_insertion_point(module_scope)
