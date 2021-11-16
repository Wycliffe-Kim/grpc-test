from ..container.CameraData import CameraData
from .IStore import IStore;

class CameraStore(IStore):
    cameras: dict[int, CameraData];
    
    def _init(self):
        self.cameras = dict()
        
    def get_cameras(self):
        return self.cameras
      
    def get_camera(self, id: int):
        camera: CameraData = self.cameras.get(id)
        return camera
        
    def set_camera(self, camera: CameraData):
        self.cameras[camera.id] = camera