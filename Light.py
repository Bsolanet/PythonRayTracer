from Vector import Vector

class Light:
    __slots__ = ('direction', 'intensity')

    #constructor
    def __init__(self, direction: Vector, intensity: int | float):
        self.direction = direction
        self.intensity = intensity

    #toString
    def __repr__(self) -> str:
        return f"Light(direction: {self.direction}, intensity: {self.intensity})"