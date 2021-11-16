class CameraPosition:
    __latitude: float
    __longitude: float
    
    def __init__(self, latitude: float, longitude: float):
        self.__latitude = latitude
        self.__longitude = longitude
        
    def __str__(self):
        return str(
            f"latitude: {self.__latitude}, "
            f"longitude: {self.__longitude}")
        
    @property
    def latitude(self):
        return self.__latitude
      
    @property
    def longitude(self):
        return self.__longitude