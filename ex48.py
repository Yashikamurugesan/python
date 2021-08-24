from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
a=np.array([0,1,2,3,4])
print('a.array : ',a)
b=np.array([0,1,2,3,4])
print('b.array : ',b)
A,B=np.meshgrid(a,b)
print('A',A)
print('B',B)
plt.plot(A,B,'or')
plt.show()
