# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secgcs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='secgcs.proto',
  package='',
  serialized_pb='\n\x0csecgcs.proto\"\x8b\x01\n\x07QGCData\x12\x10\n\x08msg_type\x18\x01 \x02(\t\x12\x10\n\x08latitude\x18\x02 \x02(\x01\x12\x11\n\tlongitude\x18\x03 \x02(\x01\x12\x0f\n\x07heading\x18\x04 \x02(\x01\x12\x10\n\x08\x61ltitude\x18\x05 \x02(\x01\x12\x14\n\x0coutside_temp\x18\x06 \x01(\x05\x12\x10\n\x08\x62\x61tt_tmp\x18\x07 \x01(\x05')




_QGCDATA = _descriptor.Descriptor(
  name='QGCData',
  full_name='QGCData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='QGCData.msg_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='QGCData.latitude', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='QGCData.longitude', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='QGCData.heading', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='QGCData.altitude', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outside_temp', full_name='QGCData.outside_temp', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batt_tmp', full_name='QGCData.batt_tmp', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['QGCData'] = _QGCDATA

class QGCData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QGCDATA

  # @@protoc_insertion_point(class_scope:QGCData)


# @@protoc_insertion_point(module_scope)
