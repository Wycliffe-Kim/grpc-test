from ..type.ScenarioType import ScenarioType

class ScenarioData:
    __id: int
    __type: ScenarioType
    
    def __init__(self, 
                 id: int, 
                 type: ScenarioType):
        self.__id = id
        self.__type = type
        
    def __str__(self):
        return str(
            f"id: {self.__id}, "
            f"type: {self.__type}")
        
    @property
    def id(self):
        return self.__id
      
    @property
    def type(self):
        return self.__type