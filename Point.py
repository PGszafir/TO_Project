# import self as self
from Vector import *

class Point:
    def __int__(self, vector):
        self.location = vector

    def __init__(self, location=[0, 0, 0]):
        self.location = Vector3D(location)
    '''    def __init__(self, x, y, z):
        self.location = Vector3D([x, y, z])


    '''


    '''    def __add__(self, other):
        addition = []
        for i in range(3):
            addition.append(self.location[i]+other.location[i])
        return addition

    def __sub__(self, other):
        substraction = []
        for i in range(3):
            substraction.append(self.location[i]-other.location[i])
        return substraction

    def __abs__(self):
        return (self.location[0]**2+self.location[1]**2+self.location[2]**2)**0.5
'''


class Material_Point(Point):
    def __init__(self):
        pass