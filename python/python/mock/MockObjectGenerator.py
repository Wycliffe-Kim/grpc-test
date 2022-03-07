from typing import Callable
from ..function.generate_random_number import generate_random_number
from ..module.WorkerThread import WorkerThread
from ..container.ObjectData import ObjectData
from ..container.Coordinate import Coordinate

class MockObjectGenerator(WorkerThread):
    __callbacks: list[Callable[[ObjectData], None]]
    
    def __new__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            self._instance = super().__new__(self)
        return self._instance

    def __init__(self):
        if not hasattr(self, "_isinit"):
            self._isinit = False

        if self._isinit == False:
            self.__init()
            self._isinit = True
                
    def __init(self):
        super().__init__('MockObjectGenerator')
        self.__callbacks = []
        self._period_ms = 500
        
    def add_callback(self, callback: Callable[[ObjectData], None]):
        self.__callbacks.append(callback)
        
    def _do_job(self):
        object_id = self.__generate_random_number()
        object_coordinate = self.__generate_random_coordinate()
        trajectory = []
        prediction_path = []
        for i in range(10):
            trajectory.append(self.__generate_random_coordinate())
            prediction_path.append(self.__generate_random_coordinate())
        object_data = ObjectData(object_id, object_coordinate, trajectory, prediction_path)
        for callback in self.__callbacks:
            callback(object_data)
            
    def __generate_random_number(self, *, min: int = 0, max: int = 100):
        return int(generate_random_number(min=float(min), max=float(max)))
    
    def __generate_random_coordinate(self):
        return Coordinate(generate_random_number(), generate_random_number())