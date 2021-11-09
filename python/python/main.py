from concurrent import futures
import grpc
import proto.test_pb2
import proto.test_pb2_grpc

class Servicer(proto.test_pb2_grpc.TestServiceServicer):
    def TestService(self, request, context):
        id = request.id
        name = request.name
        print(f'----- grpc server request id: {id}, name: {name}')
        return proto.test_pb2.TestResponse(id=id, name=name, message=f'id={id}&name={name}')
      
def serve():
    address = '[::]:7070'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto.test_pb2_grpc.add_TestServiceServicer_to_server(Servicer(), server)
    server.add_insecure_port(address)
    server.start()
    print(f'----- grpc server start {address} -----');
    server.wait_for_termination()
    
serve()