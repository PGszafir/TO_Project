import matplotlib.pyplot as plt
from Interface import *
from mesh import *
#import matplotlib as plt
from operations import *
from draw3d import *

#if __name__ == '__main__':
gui = Interface()
gui.setup_()
gui.run()

print(gui.r, gui.nop, gui.figure)
i, r, type = gui.get_values()


vector0 = Vector([0, 0, 0])
point0 = Point(vector0)
a = Draw
scene = Cuboid(point0, 6, 4, 4)

cube1 = Cube(point0, 2)
particles = Particles(vector0, 0)
#particles.emition_from_surface(50)
for frame in range(0, 1000):
   # ax.view_init(30, 90)
   if frame%10 == 0:
      particles.emition_from_surface(i)
   plt.cla()
   a.draw(scene)
   a.draw(cube1)
   plt.draw()
   a.draw(particles, 'r', '.')
   particles.step()
   plt.pause(.001)
plt.show()

#a = Draw
   #draw(particles,'y','.')