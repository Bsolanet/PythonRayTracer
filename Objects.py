from math import sqrt

from Vector import Vector
from Ray import Ray

class Sphere:
    __slots__ = ('center', 'radius', 'color', 'reflect')

    #constructor
    def __init__(self, center: Vector, radius: int | float, color: Vector, reflect: int):
        self.center = center
        self.radius = radius
        self.color = color
        self.reflect = reflect
    
    #toString
    def __repr__(self) -> str:
        return f"Sphere(center: {self.center}, radius: {self.radius}, color: {self.color}, reflect: {self.reflect})"
    
    def intersection(self, ray: Ray) -> bool | Vector:
        #set up quadratic function
        #A
        a = ray.direction.redot()
        #B
        b = 2 * (ray.origin - self.center).dot(ray.direction)
        #D
        d = (ray.origin - self.center).redot() - self.radius ** 2
        root = b ** 2 - 4 * a * d
        #no intersection
        if root < 0:
            return False
        root = sqrt(root)
        t0 = (root - b) / (2 * a)
        t1 = (root + b) / (2 * a)
        #object is behind camera
        if t0 < 0 and t1 < 0:
            return False
        
        t = t0
        if t0 < 0 or t0 < t1:
            t = t1
        
        return ray.point(t)
    
    def get_color(self, hit_position: Vector) -> Vector:
        return self.color
    
    def get_normal(self, hit_position: Vector) -> Vector:
        return (hit_position - self.center).normalize()

    def get_reflect(self) -> int:
        return self.reflect

class Plane:
    __slots__ = ('p0', 'normal', 'color', 'reflect')

    #constructor
    def __init__(self, p0: Vector, normal: Vector, color: Vector, reflect: int):
        self.p0 = p0
        self.normal = normal
        self.color = color
        self.reflect = reflect

    #toString
    def __repr__(self) -> str:
        return f"Plane(p0: {self.p0}, normal: {self.normal}, color: {self.color}, reflect: {self.reflect})"
    
    #intersection function
    def intersection(self, ray : Ray) -> bool | Vector:
        if(ray.direction.y < 0):
            return False
        denominator = ray.direction.dot(self.normal)
        #if denominator is 0, no intersection
        if(denominator == 0):
            return False
        numerator = (self.p0 - ray.origin).dot(self.normal)
        t = numerator / denominator
        return ray.point(t)
        

    #returns plane color
    def get_color(self, hit_position: Vector) -> Vector:
        return self.color
    
    #planes have constant normals
    def get_normal(self, hit_position: Vector) -> Vector:
        return self.normal
    
    def get_reflect(self) -> int:
        return self.reflect

class Triangle:
    __slots__ = ('a', 'b', 'c', 'color', 'reflect')

    #constructor
    def __init__(self, a: Vector, b: Vector, c: Vector, color: Vector, reflect: int):
        self.a = a
        self.b = b
        self.c = c
        self.color = color
        self.reflect = reflect

    #toString
    def __repr__(self) -> str:
        return f"Triangle(a: {self.a}, b: {self.b}, c: {self.c}, color: {self.color}, reflect: {self.reflect})"

    
    #intersection function
    def intersection(self, ray: Ray) -> bool | Vector:
        normal = self.get_normal()
        denominator = ray.direction.dot(normal)
        if(denominator == 0):
            return False
        numerator = (self.a - ray.origin).dot(normal)
        t = numerator / denominator
        #point on plane with points a, b, c
        p = ray.point(t)
        #figure out if it is in the triangle
        u = p - self.a
        v = self.b - self.a
        w = self.c - self.a

        vxw = v.cross(w)

        s = (vxw.dot(u.cross(w))) / (vxw.redot())
        t = (vxw.dot(v.cross(u))) / (vxw.redotdot())

        if s < 0:
            return False
        if t < 0:
            return False
        if (s + t) > 1:
            return False
        return p




    #color getter
    def get_color(self, hit_position: Vector) -> Vector:
        return self.color
    
    #normal getter
    def get_normal(self, hit_position: Vector) -> Vector:
        ab = b - a
        ac = c - a
        return ab.cross(ac)

    def get_reflect(self) -> int:
        return self.reflect
        
        