import grpc
import test_pb2_grpc
import camera_pb2_grpc
import scenario_pb2_grpc
import event_pb2_grpc
import object_pb2_grpc

from concurrent import futures
from .container.CameraData import CameraData
from .container.CameraPosition import CameraPosition
from .function.generate_random_number import generate_random_number
from .store.CameraStore import CameraStore
from .container.ScenarioData import ScenarioData
from .store.ScenarioStore import ScenarioStore
from .type.ScenarioType import ScenarioType
from .GRPCServices.TestService import TestService
from .GRPCServices.CameraService import CameraService
from .GRPCServices.ScenarioService import ScenarioService
from .GRPCServices.EventService import EventService
from .GRPCServices.ObjectService import ObjectService
from .mock.MockEventGenerator import MockEventGenerator
from .mock.MockObjectGenerator import MockObjectGenerator

def load_cameras():
    for i in range(10):
        camera = CameraData(i + 1, f'camera[{i + 1}]', CameraPosition(generate_random_number(max=180.0),generate_random_number(max=180.0)), '000.000.000.000', 554, 'admin', 'admin')
        
        CameraStore().set_camera(camera)

def load_scenarios():
    scenario = ScenarioData(1, ScenarioType.ACCIDENT)
    ScenarioStore().set_scenario(scenario)
    
def register_service(server):
    test_service = TestService()
    camera_service = CameraService()
    scenario_service = ScenarioService()
    event_service = EventService()
    object_service = ObjectService()
    
    MockEventGenerator().add_callback(event_service.event_data_received)
    MockObjectGenerator().add_callback(object_service.object_data_received)
    
    MockEventGenerator().start()
    MockObjectGenerator().start()
    
    test_pb2_grpc.add_TestServiceServicer_to_server(test_service, server)
    camera_pb2_grpc.add_CameraServiceServicer_to_server(camera_service, server)
    scenario_pb2_grpc.add_ScenarioServiceServicer_to_server(scenario_service, server)
    event_pb2_grpc.add_EventServiceServicer_to_server(event_service, server)
    object_pb2_grpc.add_ObjectServiceServicer_to_server(object_service, server)
      
def serve():
    address = '[::]:7070'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    register_service(server)
    
    server.add_insecure_port(address)
    server.start()
    print(f'----- grpc server start {address} -----');
    server.wait_for_termination()
    
def main():
    load_scenarios()
    load_cameras()
    
    serve()
    
main()