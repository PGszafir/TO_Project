from Point import *
from operations import *

class Mesh:
    def __init__(self, location):
        self.center = Point(location)
        self.verticles = []
        self.edges = []
        self.surfaces = []

    def get_verticles(self):
        points = []
        for i in self.verticles:
            points.append(i+self.center)
            print(points[-1].getComponents())

        return points


class Cube(Mesh):

    def __init__(self, location, a):
        self.center = Point(location)
        self.verticles = []
        self.edges = []
        self.surfaces = []
        for i in range(8):
            b = a/2
            bit = int_split_nr(i, 3)
            x, y, z = (-1)**bit[2]*b, (-1)**bit[1]*b, (-1)**bit[0]*b
            # print(x, y, z)
            self.verticles.append(Point([x, y, z]))