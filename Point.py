# import self as self
from Vector import *

class Point:
    def __int__(self, vector):
        self.location = vector

    def __init__(self, location=[0, 0, 0]):
        self.location = Vector(location)

    def getComponents(self):
        return self.location.getComponents()

    def getLocationVector(self):
        return self.location

    def __getitem__(self, item):
        return self.location.getComponents()[item]

    def __add__(self, other):
        vector = self.getLocationVector() + other.getLocationVector()
        return Point(vector)



    '''    def __init__(self, x, y, z):
        self.location = Vector3D([x, y, z])



    def __sub__(self, other):
        substraction = []
        for i in range(3):
            substraction.append(self.location[i]-other.location[i])
        return substraction

    def __abs__(self):
        return (self.location[0]**2+self.location[1]**2+self.location[2]**2)**0.5
'''


class Material_Point(Point):
    def __init__(self, location, mass, r, speed=Vector([0, 0, 0])):
        self.location = location
        self.mass = mass
        self.r = r
        self.speed = speed

    def step(self):
        self.location = self.location+self.speed