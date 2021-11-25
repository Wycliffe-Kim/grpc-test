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
    
    def pop_all(self) -> list[T]:
        arr: list[T] = self._data_list.copy()
        self.clear()
        return arr
    
    def peek(self, count) -> list[T]:
        arr: list[T] = []
        
        i = 0
        while i < count:
            arr.append(self._data_list[i])
            
        return arr
    
    def peek_reverse(self, count) -> list[T]:
        arr: list[T] = []
        
        i = self.count() - count
        while i < self.count():
            arr.append(self._data_list[i])
            
        return arr
      
    def clear(self):
        self._data_list.clear()
        
    def count(self):
        return len(self._data_list)