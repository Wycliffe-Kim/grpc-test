from .Coordinate import Coordinate
from ..type.ObjectType import ObjectType
from .BoundingBox import BoundingBox

class ObjectData:
    __id: int
    __type: ObjectType
    __bbox: BoundingBox
    __trajectory: list[Coordinate]
    __prediction_path: list[Coordinate]
    
    def __init__(self,
                 id: int,
                 type: ObjectType,
                 bbox: BoundingBox,
                 trajectory: list[Coordinate],
                 prediction_path: list[Coordinate]):
        self.__id = id
        self.__type = type
        self.__bbox = bbox
        self.__trajectory = trajectory
        self.__prediction_path = prediction_path
        
    def __str__(self):
        return str(
            f"id: {self.__id}, "
            f"type: {self.__type}, "
            f"bbox: {self.__bbox}, "
            f"trajectory: {self.__trajectory}, "
            f"prediction_path: {self.__prediction_path}")
        
    @property
    def id(self):
        return self.__id
    
    @property
    def type(self):
        return self.__type
    
    @property
    def bbox(self):
        return self.__bbox
      
    @property
    def trajectory(self):
        return self.__trajectory
      
    @property
    def prediction_path(self):
        return self.__prediction_path