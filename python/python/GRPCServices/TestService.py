import test_pb2
import test_pb2_grpc

class TestService(test_pb2_grpc.TestServiceServicer):
    def request(self, req, context):
        id = req.id
        name = req.name
        print(f'----- grpc server request id: {id}, name: {name}')
        return test_pb2.TestResponse(id=id, name=name, message=f'id={id}&name={name}', li=[1, 2, 3])
    
    def request_stream(self, req, context):
        id = req.id
        name = req.name
        print(f'----- grpc server request_stream id: {id}, name: {name}')
        for i in range(10):
            yield test_pb2.TestResponse(id=id, name=name, message=f'id={id}&name={name}&index={i}')