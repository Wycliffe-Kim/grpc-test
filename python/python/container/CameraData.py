from ..container.CameraPosition import CameraPosition

class CameraData:
    __id: int
    __name: str
    __position: CameraPosition
    __rtsp_address: str
    __rtsp_port: int
    __rtsp_connection_id: str
    __rtsp_connection_pw: str
    
    def __init__(self, 
                 id: int, 
                 name: str, 
                 position: CameraPosition,
                 rtsp_address: str, 
                 rtsp_port: int,
                 rtsp_connection_id: str, 
                 rtsp_connection_pw: str):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__rtsp_address = rtsp_address
        self.__rtsp_port = rtsp_port
        self.__rtsp_connection_id = rtsp_connection_id
        self.__rtsp_connection_pw = rtsp_connection_pw
        
    def __str__(self):
        return str(
            f"id: {self.__id}, "
            f"name: {self.__name}, "
            f"position: {self.__position}, "
            f"rtsp_address: {self.__rtsp_address}, "
            f"rtsp_port: {self.__rtsp_port}, "
            f"rtsp_connection_id: {self.__rtsp_connection_id}, "
            f"rtsp_connection_pw: {self.__rtsp_connection_pw}")
        
    @property
    def id(self):
        return self.__id
      
    @property
    def name(self):
        return self.__name
      
    @property
    def position(self):
        return self.__position
      
    @property
    def rtsp_address(self):
        return self.__rtsp_address
    
    @property
    def rtsp_port(self):
        return self.__rtsp_port
      
    @property
    def rtsp_connection_id(self):
        return self.__rtsp_connection_id
      
    @property
    def rtsp_connection_pw(self):
        return self.__rtsp_connection_pw
