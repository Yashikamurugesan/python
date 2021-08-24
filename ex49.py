import matplotlib.pyplot as plt
import numpy as np
#x=sin(2*3.14(x+y))
x=np.linspace(0,1,50)
print('x : ',x)
y=np.linspace(0,1,50)
print('y : ',y)
X,Y=np.meshgrid(x,y)
z=np.sin(2*np.pi*(X+Y))
print('XYZ : ',plt.plot(x,y,z))
plt.show()

