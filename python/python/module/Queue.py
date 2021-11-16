from typing import Generic, TypeVar
T = TypeVar('T')

class Queue(Generic[T]):
    _data_list: list[T]
    _max_size: int
    
    def __init__(self, max_size: int = 10000):
        self._max_size = max_size
        self._data_list = list()
        
    def __len__(self):
        return self.count()
        
    def push(self, data: T):
        if self.count() >= self._max_size:
            return
        
        self._data_list.append(data)
        
    def pop(self) -> T:
        return self._data_list.pop(0)
      
    def clear(self):
        self._data_list.clear()
        
    def count(self):
        return len(self._data_list)