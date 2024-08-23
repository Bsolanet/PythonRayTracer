from Vector import Vector

class Ray:
    __slots__ = ('origin', 'direction')

    #constructor
    def __init__(self, origin : Vector, direction: Vector):
        self.origin = origin
        self.direction = direction.normalize()

    #toString
    def __repr__(self) -> str:
        return f"Ray(origin: {self.origin}, direction: {self.direction})"
    
    #cast function
    def cast(self, objects:list) -> tuple:
        for object in objects:
            intersect = object.intersection(self)
            if intersect:
                return intersect, object
        return False, False
    
    #function to get point on ray
    def point(self, t: int | float) -> Vector:
        return self.origin + (self.direction * t)