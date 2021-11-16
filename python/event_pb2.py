# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='event.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x65vent.proto\"\x0e\n\x0c\x45ventRequest\"b\n\tEventData\x12\x15\n\roccurred_time\x18\x01 \x01(\t\x12\x16\n\x0eobject_id_list\x18\x02 \x03(\x05\x12\x11\n\tcamera_id\x18\x03 \x01(\x05\x12\x13\n\x0bscenario_id\x18\x04 \x01(\x05\x32@\n\x0c\x45ventService\x12\x30\n\x0fstreaming_event\x12\r.EventRequest\x1a\n.EventData\"\x00\x30\x01\x62\x06proto3'
)




_EVENTREQUEST = _descriptor.Descriptor(
  name='EventRequest',
  full_name='EventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=29,
)


_EVENTDATA = _descriptor.Descriptor(
  name='EventData',
  full_name='EventData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='occurred_time', full_name='EventData.occurred_time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_id_list', full_name='EventData.object_id_list', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='camera_id', full_name='EventData.camera_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scenario_id', full_name='EventData.scenario_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['EventRequest'] = _EVENTREQUEST
DESCRIPTOR.message_types_by_name['EventData'] = _EVENTDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventRequest = _reflection.GeneratedProtocolMessageType('EventRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREQUEST,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:EventRequest)
  })
_sym_db.RegisterMessage(EventRequest)

EventData = _reflection.GeneratedProtocolMessageType('EventData', (_message.Message,), {
  'DESCRIPTOR' : _EVENTDATA,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:EventData)
  })
_sym_db.RegisterMessage(EventData)



_EVENTSERVICE = _descriptor.ServiceDescriptor(
  name='EventService',
  full_name='EventService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=131,
  serialized_end=195,
  methods=[
  _descriptor.MethodDescriptor(
    name='streaming_event',
    full_name='EventService.streaming_event',
    index=0,
    containing_service=None,
    input_type=_EVENTREQUEST,
    output_type=_EVENTDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTSERVICE)

DESCRIPTOR.services_by_name['EventService'] = _EVENTSERVICE

# @@protoc_insertion_point(module_scope)
