class IStore:
    def __new__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            self._instance = super().__new__(self)
        return self._instance

    def __init__(self):
        if not hasattr(self, "_isinit"):
            self._isinit = False
            
        if self._isinit == False:
            self._init()
            self._isinit = True

    def _init(self):
        pass