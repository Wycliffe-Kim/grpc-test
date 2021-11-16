import camera_pb2
import camera_pb2_grpc

from ..container.CameraData import CameraData
from ..store.CameraStore import CameraStore

class CameraService(camera_pb2_grpc.CameraServiceServicer):
    def get_camera(self, request, context):
        camera_id = request.id
        camera = CameraStore().get_camera(camera_id)
        return self.__to_grpc_camera_data(camera)
      
    def get_cameras(self, request, context):
        print('----- grpc server camera service get_cameras -----')
        cameras = CameraStore().get_cameras()
        camera_response = []
        for camera in cameras.values():
            camera_response.append(self.__to_grpc_camera_data(camera))
        return camera_pb2.CameraResponse(data=camera_response)
      
    def __to_grpc_camera_data(self, camera: CameraData):
        return camera_pb2.CameraData(
          id=camera.id, 
          name=camera.name, 
          position=camera_pb2.CameraPosition(
            latitude=camera.position.latitude, 
            longitude=camera.position.longitude
          ), 
          rtsp_address=camera.rtsp_address, 
          rtsp_port=camera.rtsp_port, 
          rtsp_connection_id=camera.rtsp_connection_id, 
          rtsp_connection_pw=camera.rtsp_connection_pw)