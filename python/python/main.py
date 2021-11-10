from concurrent import futures
import grpc
import test_pb2
import test_pb2_grpc

class TestService(test_pb2_grpc.TestServiceServicer):
    def request(self, req, context):
        id = req.id
        name = req.name
        print(f'----- grpc server request id: {id}, name: {name}')
        return test_pb2.TestResponse(id=id, name=name, message=f'id={id}&name={name}')
      
def serve():
    address = '[::]:7070'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)
    server.add_insecure_port(address)
    server.start()
    print(f'----- grpc server start {address} -----');
    server.wait_for_termination()
    
serve()