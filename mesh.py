from Point import *
from operations import *
import random as rand

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


class Cuboid(Mesh):
    def __init__(self, location, a, b, c):
        self.center = Point(location)
        self.verticles = []
        self.edges = []
        self.surfaces = []
        for i in range(8):
            bit = int_split_nr(i, 3)
            x, y, z = (-1)**bit[2]*a/2, (-1)**bit[1]*b/2, (-1)**bit[0]*c/2
            # print(x, y, z)
            self.verticles.append(Point([x, y, z]))


class Particles(Mesh):
    def __init__(self, location, surface):
        self.center = Point(location)
        self.verticles = []
        self.surfaces = surface

    def emition_from_surface(self, count):
        mass = 0.01
        speed = Vector([-1, 0, 0])
        r = 0.01
        for i in range(count):
            location = Vector([3, (rand.random()-0.5)*4, (rand.random()-0.5)*4]) # !!!

            self.verticles.append(Material_Point(location,mass, r, speed))

    def step(self):
        for i in self.verticles:
            i.step()