import unittest
from operations import *

class MyTestCase(unittest.TestCase):
    def test_int_split(self):
        self.assertEqual(int_split(12), [0, 0, 1, 1])  # add assertion here

    def test_int_split_0(self):
        self.assertEqual(int_split(0), [])

if __name__ == '__main__':
    unittest.main()


'''from mpl_toolkits.mplot3d import axes3d

import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# load some test data for demonstration and plot a wireframe
X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)

# rotate the axes and update
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)'''
