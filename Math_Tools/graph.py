import numpy as np
import matplotlib.pyplot as plt

u_start = 0
u_end = 3
u_detail = 100
u = np.linspace(u_start, u_end, u_detail)   #parameter 1

v_start = 0
v_end = np.pi
v_detail = 100
v = np.linspace(v_start, v_end, v_detail)   #parameter 2

x_1 = u
x_2 = (np.cos(v))**2
(x_1, x_2) = np.meshgrid(x_1, x_2)
x = x_1 * x_2
y_1 = u
y_2 = (np.sin(v))**2
(y_1, y_2) = np.meshgrid(y_1, y_2)
y = y_1 * y_2
z_1 = u
z_2 = v
z = idk_man    #defining functions. ax.plot_surface requires z to be a 2d array made by meshgrid (works like a matrix i think)

#basically trying to make it not be (x(u), y(v), z(x, y)), but struggling

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

surface = ax.plot_surface(x, y, z, cmap="coolwarm", linewidth=0, antialiased=False)

plt.show()