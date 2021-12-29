from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw(figure):
    xs, ys, zs = [], [], []

    for i in figure.get_verticles():
        xs.append(i.getComponents()[0])
        ys.append(i.getComponents()[1])
        zs.append(i.getComponents()[2])
        ax.scatter(xs, ys, zs, c='c', marker='^')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    #plt.show()

