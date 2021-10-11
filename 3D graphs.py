from mpl_toolkits import mplot3d
import numpy ad np
import matplotlib.pyplot as plt

x=np.outer(np.linspace(-2,2,10),np.ones(10))
y=x.copy().T
z=np.cos(x**2+y**3)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,z,camp='viridis',edgecolor='back')
plt.show()
