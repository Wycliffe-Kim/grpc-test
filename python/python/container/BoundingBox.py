class BoundingBox:
    __x: float
    __y: float
    __width: float
    __height: float
    
    def __init__(self, 
                 x: float, 
                 y: float, 
                 width: float, 
                 height: float):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        
    def __str__(self):
        return str(
          f"x: {self.__x}, "
          f"y: {self.__y}, "
          f"width: {self.__width}, "
          f"height: {self.__height}")
        
    @property
    def x(self):
        return self.__x
      
    @property
    def y(self):
        return self.__y
      
    @property
    def width(self):
        return self.__width
      
    @property
    def height(self):
        return self.__height