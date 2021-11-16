from ..container.ObjectCoordinate import ObjectCoordinate

class ObjectData:
    __id: int
    __coordinate: ObjectCoordinate
    __trajectory: list[ObjectCoordinate]
    __prediction_path: list[ObjectCoordinate]
    
    def __init__(self,
                 id: int,
                 coordinate: ObjectCoordinate,
                 trajectory: list[ObjectCoordinate],
                 prediction_path: list[ObjectCoordinate]):
        self.__id = id
        self.__coordinate = coordinate
        self.__trajectory = trajectory
        self.__prediction_path = prediction_path
        
    def __str__(self):
        return str(
            f"id: {self.__id}, "
            f"coordinate: {self.__coordinate}, "
            f"trajectory: {self.__trajectory}, "
            f"prediction_path: {self.__prediction_path}")
        
    @property
    def id(self):
        return self.__id
      
    @property
    def coordinate(self):
        return self.__coordinate
      
    @property
    def trajectory(self):
        return self.__trajectory
      
    @property
    def prediction_path(self):
        return self.__prediction_path