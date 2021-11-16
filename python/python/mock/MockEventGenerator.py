from datetime import datetime
from typing import Callable
from ..function.generate_random_number import generate_random_number
from ..module.WorkerThread import WorkerThread
from ..container.EventData import EventData

class MockEventGenerator(WorkerThread):
    __callbacks: list[Callable[[EventData], None]]
    
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
        super().__init__('MockEventGenerator')
        self.__callbacks = []
        self._period_ms = 5000
        
    def add_callback(self, callback: Callable[[EventData], None]):
        self.__callbacks.append(callback)
        
    def _do_job(self):
        object_id_list = [self.__generate_random_number(), self.__generate_random_number()]
        camera_id = self.__generate_random_number(min=1, max=10)
        scenario_id = 1
        event_data = EventData(datetime.now(), object_id_list, camera_id, scenario_id)
        for callback in self.__callbacks:
            callback(event_data)
            
    def __generate_random_number(self, *, min: int = 0, max: int = 100):
        return int(generate_random_number(min=float(min), max=float(max)))