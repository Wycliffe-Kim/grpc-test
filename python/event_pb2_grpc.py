# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import event_pb2 as event__pb2


class EventServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.streaming_event = channel.unary_stream(
                '/EventService/streaming_event',
                request_serializer=event__pb2.EventRequest.SerializeToString,
                response_deserializer=event__pb2.EventData.FromString,
                )


class EventServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def streaming_event(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'streaming_event': grpc.unary_stream_rpc_method_handler(
                    servicer.streaming_event,
                    request_deserializer=event__pb2.EventRequest.FromString,
                    response_serializer=event__pb2.EventData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EventService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def streaming_event(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/EventService/streaming_event',
            event__pb2.EventRequest.SerializeToString,
            event__pb2.EventData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
