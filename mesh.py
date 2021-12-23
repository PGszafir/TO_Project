from Point import *
from operations import *

class Mesh:
    def __init__(self,location):
        self.center = Point(location)

class Cube(Mesh):
    def __init__(self, location, a):
        self.center = Point(location)
        self.verticles = []
        for i in range(8):
            b=a/2
            bit=int_split(i)
            x,y,z=(-1)**bit[2]*b,(-1)**bit[1]*b,(-1)**bit[0]*b # !!! out of range
            self.verticles.append(Point([x,y,z]))
