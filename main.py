import matplotlib.pyplot as plt

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
particles.emition_from_surface(20)
if __name__ == '__main__':
   #draw(cube1)
   #draw(cube2)
   #draw(cuboid)


   #draw(particles,'y','.')

   for frame in range(0, 10000):
      # ax.view_init(30, 90)
      plt.cla()
      draw(cuboid)
      draw(cube1)
      plt.draw()
      draw(particles, 'r', '.')
      particles.step()
      plt.pause(.001)

   plt.show()
