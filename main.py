from mesh import *
#import matplotlib as plt
from operations import *
from draw3d import *

vector0 = Vector([0, 0, 0])
vector1 = Vector([0, 0, 0])

point0 = Point(vector0)
point1 = Point(vector1)

cube1 = Cube(point0, 2)
cube2 = Cube(point1, 1)
cuboid = Cuboid(point0, 6, 4 , 4)
particles = Particles(vector1, 0)
particles.emition_from_surface(200)
if __name__ == '__main__':
   draw(cube1)
   draw(cube2)
   draw(cuboid)

   draw(particles,'r','.')
   particles.step()
   draw(particles,'y','.')
   plt.show()
