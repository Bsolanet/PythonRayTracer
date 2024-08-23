from math import tan, radians

from Vector import Vector
from Ray import Ray

class Camera:
    __slots__ = ('position', 'screen_size', 'fov')

    #constructor
    def __init__(self, position: Vector, screen_size: Vector, fov: int | float = 60.0):
        self.position = position
        self.screen_size = screen_size
        self.fov = fov
    
    #toString
    def __repr__(self) -> str:
        return f"Camera(postition: {self.position}, screen size: {self.screen_size}, field of view: {self.fov})"
    
    #get direction of the camera
    def get_direction(self, v: Vector) -> Ray:
        xy = v - self.screen_size / 2
        z = self.screen_size.y / tan(radians(self.fov) / 2)
        return Ray(self.position, Vector(xy.x, xy.y, -z).normalize())