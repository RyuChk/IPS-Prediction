# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ips.user.v1 import user_pb2 as ips_dot_user_dot_v1_dot_user__pb2


class UserManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCoordinate = channel.unary_unary(
                '/ips.user.v1.UserManagerService/GetCoordinate',
                request_serializer=ips_dot_user_dot_v1_dot_user__pb2.GetCoordinateRequest.SerializeToString,
                response_deserializer=ips_dot_user_dot_v1_dot_user__pb2.GetCoordinateResponse.FromString,
                )
        self.RegisterAp = channel.unary_unary(
                '/ips.user.v1.UserManagerService/RegisterAp',
                request_serializer=ips_dot_user_dot_v1_dot_user__pb2.RegisterApRequest.SerializeToString,
                response_deserializer=ips_dot_user_dot_v1_dot_user__pb2.RegisterApResponse.FromString,
                )


class UserManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCoordinate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterAp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCoordinate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCoordinate,
                    request_deserializer=ips_dot_user_dot_v1_dot_user__pb2.GetCoordinateRequest.FromString,
                    response_serializer=ips_dot_user_dot_v1_dot_user__pb2.GetCoordinateResponse.SerializeToString,
            ),
            'RegisterAp': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterAp,
                    request_deserializer=ips_dot_user_dot_v1_dot_user__pb2.RegisterApRequest.FromString,
                    response_serializer=ips_dot_user_dot_v1_dot_user__pb2.RegisterApResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ips.user.v1.UserManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCoordinate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ips.user.v1.UserManagerService/GetCoordinate',
            ips_dot_user_dot_v1_dot_user__pb2.GetCoordinateRequest.SerializeToString,
            ips_dot_user_dot_v1_dot_user__pb2.GetCoordinateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterAp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ips.user.v1.UserManagerService/RegisterAp',
            ips_dot_user_dot_v1_dot_user__pb2.RegisterApRequest.SerializeToString,
            ips_dot_user_dot_v1_dot_user__pb2.RegisterApResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
