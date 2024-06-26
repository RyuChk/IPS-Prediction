# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ips.map.v1 import user_tracking_pb2 as ips_dot_map_dot_v1_dot_user__tracking__pb2


class UserTrackingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddUpdateOnlineUser = channel.unary_unary(
                '/ips.map.v1.UserTrackingService/AddUpdateOnlineUser',
                request_serializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.AddUpdateOnlineUserRequest.SerializeToString,
                response_deserializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.AddUpdateOnlineUserResponse.FromString,
                )
        self.FetchOnlineUser = channel.unary_unary(
                '/ips.map.v1.UserTrackingService/FetchOnlineUser',
                request_serializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.FetchOnlineUserRequest.SerializeToString,
                response_deserializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.FetchOnlineUserResponse.FromString,
                )


class UserTrackingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddUpdateOnlineUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchOnlineUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserTrackingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddUpdateOnlineUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUpdateOnlineUser,
                    request_deserializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.AddUpdateOnlineUserRequest.FromString,
                    response_serializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.AddUpdateOnlineUserResponse.SerializeToString,
            ),
            'FetchOnlineUser': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchOnlineUser,
                    request_deserializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.FetchOnlineUserRequest.FromString,
                    response_serializer=ips_dot_map_dot_v1_dot_user__tracking__pb2.FetchOnlineUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ips.map.v1.UserTrackingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserTrackingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddUpdateOnlineUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ips.map.v1.UserTrackingService/AddUpdateOnlineUser',
            ips_dot_map_dot_v1_dot_user__tracking__pb2.AddUpdateOnlineUserRequest.SerializeToString,
            ips_dot_map_dot_v1_dot_user__tracking__pb2.AddUpdateOnlineUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchOnlineUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ips.map.v1.UserTrackingService/FetchOnlineUser',
            ips_dot_map_dot_v1_dot_user__tracking__pb2.FetchOnlineUserRequest.SerializeToString,
            ips_dot_map_dot_v1_dot_user__tracking__pb2.FetchOnlineUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
