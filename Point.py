# import self as self


class Point:
    def __init__(self, x, y, z):
        self.location = [x, y, z]

    def __init__(self, location=[0, 0, 0]):
        self.location = location

    def __add__(self, other):
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
