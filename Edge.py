from Point import *

class Edge:
    def __init__(self, a, b):
        self.points = [a, b]

    def subdivide(self,n = 2):
        c = a.getLocationVector()-b.getLocationVector()#a-b/n