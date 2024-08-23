from __future__ import annotations
from math import sqrt

class Vector:
    __slots__ = ('x', 'y', 'z')

    #constructor
    def __init__(self, x: int | float = 0.0, y: int | float = 0.0, z: int | float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    #toString
    def __repr__(self) -> str:
        return f"Vector(x: {self.x}, y: {self.y}, z: {self.z})"
    
    #add
    def __add__(self, addend: Vector | int | float) -> Vector:
        if type(addend) == int or type(addend) == float:
            return Vector(self.x + addend, self.y + addend, self.z + addend)
        elif type(addend) == Vector:
            return Vector(self.x + addend.x, self.y + addend.y, self.z + addend.z)
        return self
    
    #sub
    def __sub__(self, subtraend: Vector | int | float) -> Vector:
        if type(subtraend) == int or type(subtraend) == float:
            return Vector(self.x - subtraend, self.y - subtraend, self.z - subtraend)
        elif type(subtraend) == Vector:
            return Vector(self.x - subtraend.x, self.y - subtraend.y, self.z - subtraend.z)
        return 

    #multiply
    def __mul__(self, factor: Vector | int | float) -> Vector:
        if type(factor) == int or type(factor) == float:
            return Vector(self.x * factor, self.y * factor, self.z * factor)
        elif type(factor) == Vector:
            return Vector(self.x * factor.x, self.y * factor.y, self.z * factor.z)
        return self
    
    #division
    def __truediv__(self, divisor: Vector | int | float) -> Vector:
        if type(divisor) == int or type(divisor) == float:
            return Vector(self.x / (divisor + 0.00000000001), self.y / (divisor + 0.00000000001), self.z / (divisor + 0.00000000001))
        elif type(divisor) == Vector:
            return Vector(self.x / (divisor.x + 0.00000000001), self.y / (divisor.y + 0.00000000001), self.z / (divisor.z + 0.00000000001))
        return self

    #exponent
    def __pow__(self, exponent: Vector | int | float) -> Vector:
        if type(exponent) == int or type(exponent) == float:
            return Vector(self.x ** exponent, self.y ** exponent, self.z ** exponent)
        elif type(exponent) == Vector:
            return Vector(self.x ** exponent.x, self.y ** exponent.y, self.z ** exponent.z)
        return self

    #magnitude
    def magnitude(self):
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    #greater than
    def __gt__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() > other
        if type(other) == Vector:
            return self.magnitude() > other.magnitude
        return False
    
    #less than
    def __lt__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() < other
        if type(other) == Vector:
            return self.magnitude() < other.magnitude
        return False

    #greater than or equal
    def __gte__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() >= other
        if type(other) == Vector:
            return self.magnitude() >= other.magnitude
        return False

    #less than or equal
    def __lte__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() <= other
        if type(other) == Vector:
            return self.magnitude() <= other.magnitude
        return False

    #equal to
    def __gt__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() == other
        if type(other) == Vector:
            return self.magnitude() == other.magnitude
        return False

    #negation
    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    #absolute value
    def __pos__(self) -> Vector:
        return Vector(+self.x, +self.y, +self.z)
    
    #return magnitude as a float
    def __float__(self) -> float:
        return float(self.magnitude())
    
    #return magnitude as an int
    def __int__(self) -> int:
        return int(self.magnitude())
    
    #dot product
    def dot(self, factor: Vector | int | float) -> int | float:
        if type(factor) == int or type(factor) == float:
            return self.x * factor + self.y * factor + self.z * factor
        if type(factor) == Vector:
            return self.x * factor.x + self.y * factor.y + self.z * factor.z
        return self.x + self.y + self.z

    #reflexive dot
    def redot(self) -> int | float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2
    
    #cross product
    def cross(self, factor: Vector) -> Vector:
        return Vector((self.y * factor.z) - (self.z - factor.z), (self.z * factor.x) - (self.x * factor.z), (self.x * factor.y) - (self.y * factor.x))

    #normalize
    def normalize(self) -> Vector:
        return self / self.magnitude()

    #reflection across normal vector
    def reflect(self, normal: Vector) -> Vector:
        return self - (normal * self.dot(normal) * 2)
    
    #convert vector to rgb value
    def to_rgb(self) -> tuple:
        r, g, b = self.x, self.y, self.z
        if r < 0: r = 0
        elif r > 1: r = 1
        if g < 0: g = 0
        elif g > 1: g = 1
        if b < 0: b = 0
        elif b > 1: b = 1

        return (r * 255, g * 255, b * 255)