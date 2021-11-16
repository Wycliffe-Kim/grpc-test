import event_pb2
import event_pb2_grpc

from ..container.EventData import EventData
from ..module.Queue import Queue

class EventService(event_pb2_grpc.EventServiceServicer):
    __streaming: bool
    __event_data_list: Queue[EventData]
    
    def __del__(self):
        self.__streaming = False
      
    def __init__(self):
        self.__streaming = True
        self.__event_data_list = Queue()
        
    def event_data_received(self, event_data: EventData):
        self.__event_data_list.push(event_data)
      
    def streaming_event(self, request, context):
        while self.__streaming == True:
            if self.__event_data_list.count() == 0:
                continue
              
            event_data = self.__event_data_list.pop()
              
            yield self.__to_grpc_event_data(event_data)
      
    def __to_grpc_event_data(self, event_data: EventData):
        return event_pb2.EventData(
            occurred_time=str(event_data.occurred_time),
            object_id_list=event_data.object_id_list,
            camera_id=event_data.camera_id,
            scenario_id=event_data.scenario_id)