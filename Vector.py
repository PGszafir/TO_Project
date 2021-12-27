

class Vector3D:
    def __init__(self, xyz):
        self.vector = xyz

    def abs(self):
        return (self.vector[0]**2+self.vector[1]**2+self.vector[2]**2)**0.5

    def __add__(self, other):
        x = self.vector[0]+other.getComponents[0]
        y = self.vector[1]+other.getComponents[1]
        z = self.vector[2]+other.getComponents[2]
        tab = [x, y, z]
        return Vector3D(tab)

    '''def cdot(self,v2):
        x2, y2 , z2 = v2.getComponents()
        x,y=self.__srcVector.getComponents
        x3 = x * x2
        y3 = y * y2
        z3 = self.__z * z2
        return x3+y3+z3'''

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

