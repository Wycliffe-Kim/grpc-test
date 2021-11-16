import threading
import time

from abc import *

class WorkerThread(threading.Thread, metaclass=ABCMeta):
    _period_ms: int
    _is_pause: bool
    _is_running: bool

    def __init__(self, name=''):
        super().__init__()

        self.setName(name)
        self._period_ms = 1
        self._is_pause = True
        self._is_running = False

    def __del__(self):
        self.stop()

    def run(self):
        while self._is_running == True:
            if self._is_pause == False:
                self._do_job()
            time.sleep(self._period_ms / 1000)

    def pause(self):
        self._is_pause = True

    def resume(self):
        self._is_pause = False

    def start(self):
        if self._is_running == False:
            self._is_running = True

        self.resume()
        return super().start()

    def stop(self):
        self.pause()

        if self._is_running == True:
            self._is_running = False

    @abstractmethod
    def _do_job(self):
        pass