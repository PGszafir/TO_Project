from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

class Draw:
    def __init__(self):
        print('start')

    def draw(figure, c='c', m='^'):
        #ax = fig.add_subplot(111, projection='3d')
        xs, ys, zs = [], [], []

        for i in figure.get_verticles():
            xs.append(i.getComponents()[0])
            ys.append(i.getComponents()[1])
            zs.append(i.getComponents()[2])
        ax.scatter(xs, ys, zs, c=c, marker=m)
        x=np.array(xs)
        y=np.array(ys)
        z=np.array(zs)
        #ax.plot_surface(x, y, z, c=c)
        ax.set_zlim(-3, 3)
        plt.xlim([-3, 3])
        plt.ylim([-3, 3])
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
    #plt.show()