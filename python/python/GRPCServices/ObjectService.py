import object_pb2
import object_pb2_grpc

from ..container.ObjectCoordinate import ObjectCoordinate
from ..container.ObjectData import ObjectData
from ..module.Queue import Queue

class ObjectService(object_pb2_grpc.ObjectServiceServicer):
    __streaming: bool
    __object_data_list: Queue[ObjectData]
    
    def __del__(self):
        self.__streaming = False
        
    def __init__(self):
        self.__streaming = True
        self.__object_data_list = Queue()
        
    def object_data_received(self, object_data: ObjectData):
        self.__object_data_list.push(object_data)
        
    def streaming_object(self, request, context):
        while self.__streaming == True:
            if self.__object_data_list.count() == 0:
                continue
              
            object_data = self.__object_data_list.pop()
            
            yield self.__to_grpc_object_data(object_data)
            
    def __to_grpc_object_data(self, object_data: ObjectData):
        return object_pb2.ObjectData(
            id=object_data.id,
            coordinate=self.__to_grpc_object_coordinate(object_data.coordinate),
            trajectory=self.__to_grpc_object_coordinate_list(object_data.trajectory),
            prediction_path=self.__to_grpc_object_coordinate_list(object_data.prediction_path))
        
    def __to_grpc_object_coordinate(self, object_coordinate: ObjectCoordinate):
        return object_pb2.ObjectCoordinate(
                x=object_coordinate.x,
                y=object_coordinate.y)
        
    def __to_grpc_object_coordinate_list(self, object_coordinate_list: list[ObjectCoordinate]):
        grpc_object_coordinate_list = []
        for object_coordinate in object_coordinate_list:
            grpc_object_coordinate_list.append(self.__to_grpc_object_coordinate(object_coordinate))
        
        return grpc_object_coordinate_list