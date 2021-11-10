# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test_pb2 as test__pb2


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.request = channel.unary_unary(
                '/TestService/request',
                request_serializer=test__pb2.TestRequest.SerializeToString,
                response_deserializer=test__pb2.TestResponse.FromString,
                )


class TestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def request(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'request': grpc.unary_unary_rpc_method_handler(
                    servicer.request,
                    request_deserializer=test__pb2.TestRequest.FromString,
                    response_serializer=test__pb2.TestResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TestService/request',
            test__pb2.TestRequest.SerializeToString,
            test__pb2.TestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)