# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ips/map/v1/user_tracking.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ips.shared.map.v1 import presence_pb2 as ips_dot_shared_dot_map_dot_v1_dot_presence__pb2
from ips.shared.rssi.v1 import rssi_pb2 as ips_dot_shared_dot_rssi_dot_v1_dot_rssi__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eips/map/v1/user_tracking.proto\x12\nips.map.v1\x1a ips/shared/map/v1/presence.proto\x1a\x1dips/shared/rssi/v1/rssi.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc1\x01\n\x1a\x41\x64\x64UpdateOnlineUserRequest\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x10\n\x08\x62uilding\x18\x02 \x01(\t\x12\r\n\x05\x66loor\x18\x03 \x01(\x05\x12\r\n\x05label\x18\x04 \x01(\t\x12.\n\x08position\x18\x05 \x01(\x0b\x32\x1c.ips.shared.rssi.v1.Position\x12-\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1d\n\x1b\x41\x64\x64UpdateOnlineUserResponse\"9\n\x16\x46\x65tchOnlineUserRequest\x12\x10\n\x08\x62uilding\x18\x01 \x01(\t\x12\r\n\x05\x66loor\x18\x02 \x01(\x05\"}\n\x17\x46\x65tchOnlineUserResponse\x12\x33\n\x0conline_users\x18\x01 \x03(\x0b\x32\x1d.ips.shared.map.v1.OnlineUser\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xd9\x01\n\x13UserTrackingService\x12\x66\n\x13\x41\x64\x64UpdateOnlineUser\x12&.ips.map.v1.AddUpdateOnlineUserRequest\x1a\'.ips.map.v1.AddUpdateOnlineUserResponse\x12Z\n\x0f\x46\x65tchOnlineUser\x12\".ips.map.v1.FetchOnlineUserRequest\x1a#.ips.map.v1.FetchOnlineUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ips.map.v1.user_tracking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ADDUPDATEONLINEUSERREQUEST']._serialized_start=145
  _globals['_ADDUPDATEONLINEUSERREQUEST']._serialized_end=338
  _globals['_ADDUPDATEONLINEUSERRESPONSE']._serialized_start=340
  _globals['_ADDUPDATEONLINEUSERRESPONSE']._serialized_end=369
  _globals['_FETCHONLINEUSERREQUEST']._serialized_start=371
  _globals['_FETCHONLINEUSERREQUEST']._serialized_end=428
  _globals['_FETCHONLINEUSERRESPONSE']._serialized_start=430
  _globals['_FETCHONLINEUSERRESPONSE']._serialized_end=555
  _globals['_USERTRACKINGSERVICE']._serialized_start=558
  _globals['_USERTRACKINGSERVICE']._serialized_end=775
# @@protoc_insertion_point(module_scope)