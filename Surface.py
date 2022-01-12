from Edge import *


class Surface:
    def __init__(self):
        self.edges = []
        self.vectors = []

    def getABCD(self):
        v1 = (self.vectors[1]-self.vectors[0])
        v2 = (self.vectors[2]-self.vectors[0])
        v3 = v1.cross(v2)
        a,b,c = v3.getComponents()
        d = -(a*self.vectors[0].getComponents[0]+b*self.vectors[0].getComponents[1]+c*self.vectors[0].getComponents[2])
        return [a, b, c, d]
