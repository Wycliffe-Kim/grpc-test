from ..type.ScenarioType import ScenarioType

class ScenarioData:
    __type: ScenarioType
    
    def __init__(self, type: ScenarioType):
        self.__type = type
        
    @property
    def type(self):
        return self.__type