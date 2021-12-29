import math as math

class Vector:
    def __init__(self, xyz):
        self.vector = xyz

    def abs(self):
        return (self.vector[0]**2+self.vector[1]**2+self.vector[2]**2)**0.5

    def __add__(self, other):
        print(type(self),type(other),type(self.vector[0]))
        x = self.vector[0]+other.getComponents()[0]
        y = self.vector[1]+other.getComponents()[1]
        z = self.vector[2]+other.getComponents()[2]
        tab = [x, y, z]
        return Vector(tab)

    def __sub__(self, other):
        x = self.vector[0]-other.getComponents()[0]
        y = self.vector[1]-other.getComponents()[1]
        z = self.vector[2]-other.getComponents()[2]
        tab = [x, y, z]
        return Vector(tab)

    def __getitem__(self, item):
        return self.getComponents()[item]


    def cdot(self, v2):
        x2, y2, z2 = v2.getComponents()

        x3 = self.vector[0] * x2
        y3 = self.vector[1] * y2
        z3 = self.vector[2] * z2
        return x3+y3+z3

    def getComponents(self):
        return self.vector

    def cross(self, vector): # param: IVector): #Vector3D [0,-z,y],[z,0,-x],[-y,x,0]
        x, y, z = self.vector[0],self.vector[1],self.vector[2]
        matrix = [[0, -z, y], [z, 0, -x], [-y, x, 0]]
        newVector = []
        vector2 = [0, 0, 0]
        vector2_getvalues = vector.getComponents()

        for i,a in enumerate(vector2_getvalues):
            vector2[i] = a

        sum = 0
        for a in matrix:
            for i, b in enumerate(a):
                sum = sum+b*vector2[i]
            newVector.append(sum)
            sum = 0
        return newVector

    def cos_3d(self, other):
        a = self.cdot(other)
        sum_abs = abs(self)+abs(other)
        cos_3d = a/sum_abs
        return cos_3d

    def reflection_surface(self, surface):
        pass

    def reflection_point(self, point):
        pass
