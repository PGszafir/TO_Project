import matplotlib.pyplot as plt
from Interface import *
from mesh import *
#import matplotlib as plt
from operations import *
from draw3d import *

vector0 = Vector([0,0,0])
point0 = Point(vector0)
a = Draw
cube1 = Cube(point0, 2)

scene = Cuboid(point0, 6, 4, 4)
particles = Particles(vector0, 0)
particles.emition_from_surface(100)



if __name__ == '__main__':
   gui = Interface()
   gui.run()



   #a = Draw

   #draw(particles,'y','.')

   for frame in range(0, 10000):
      # ax.view_init(30, 90)
      plt.cla()
      a.draw(scene)
      a.draw(cube1)
      plt.draw()
      a.draw(particles, 'r', '.')
      particles.step()
      plt.pause(.001)

   plt.show()
