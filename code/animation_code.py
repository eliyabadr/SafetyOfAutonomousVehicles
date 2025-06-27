import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("../refineCBF/examples/quad_2d")
from animate_quad import animate_multi_planar_quad


t = np.linspace(0, 10, 200)
x = np.array([np.sin(t), np.sin(t + 1)])
y = np.array([np.cos(t), np.cos(t + 1)])
theta = np.array([0.2 * t, 0.2 * t + 0.5])
alphas = [1.0, 0.5]
colors = ['tab:blue', 'tab:green']

fig, ani = animate_multi_planar_quad(t, x, y, theta, alphas=alphas, colors=colors)

plt.show()


