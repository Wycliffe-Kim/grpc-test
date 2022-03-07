from datetime import datetime
from ..type.ObjectType import ObjectType
from ..type.ScenarioType import ScenarioType

class EventData:
    __occurred_time: datetime
    __object_type_list: list[ObjectType]
    __camera_id: int
    __scenario: ScenarioType
    
    def __init__(self,
                 occurred_time: datetime,
                 object_type_list: list[ObjectType],
                 camera_id: int,
                 scenario: ScenarioType):
        self.__occurred_time = occurred_time
        self.__object_type_list = object_type_list
        self.__camera_id = camera_id
        self.__scenario = scenario
        
    def __str__(self):
        return str(
            f"occurred_time: {self.__occurred_time}, "
            f"object_type_list: {self.__object_type_list}, "
            f"camera_id: {self.__camera_id}, "
            f"scenario: {self.__scenario}")
        
    @property
    def occurred_time(self):
        return self.__occurred_time
      
    @property
    def object_type_list(self):
        return self.__object_type_list
      
    @property
    def camera_id(self):
        return self.__camera_id
      
    @property
    def scenario(self):
        return self.__scenario