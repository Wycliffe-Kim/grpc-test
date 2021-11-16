from datetime import datetime

class EventData:
    __occurred_time: datetime
    __object_id_list: list[int]
    __camera_id: int
    __scenario_id: int
    
    def __init__(self,
                 occurred_time: datetime,
                 object_id_list: list[int],
                 camera_id: int,
                 scenario_id: int):
        self.__occurred_time = occurred_time
        self.__object_id_list = object_id_list
        self.__camera_id = camera_id
        self.__scenario_id = scenario_id
        
    def __str__(self):
        return str(
            f"occurred_time: {self.__occurred_time}, "
            f"object_id_list: {self.__object_id_list}, "
            f"camera_id: {self.__camera_id}, "
            f"scenario_id: {self.__scenario_id}")
        
    @property
    def occurred_time(self):
        return self.__occurred_time
      
    @property
    def object_id_list(self):
        return self.__object_id_list
      
    @property
    def camera_id(self):
        return self.__camera_id
      
    @property
    def scenario_id(self):
        return self.__scenario_id