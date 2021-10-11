# Python code that compares the
# asymptotic behaviour of several functions
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Returns a function that computes x ^ n for a given n
def poly(n):
	def polyXN(x):
		return x**n
	return polyXN

# Functions to compare and colors to use in the graph
FUNCTIONS = [np.log, poly(1), poly(2), poly(3), np.exp]
COLORS = ['c', 'b', 'm', 'y', 'r']

# Plot the graphs
def compareAsymptotic(n):
	x = np.arange(1, n, 1)
	plt.title('O(n) for n ='+str(n))
	for f, c in zip(FUNCTIONS, COLORS):
		plt.plot(x, f(x), c)
	plt.show()
		
compareAsymptotic(3)
compareAsymptotic(5)
compareAsymptotic(10)
compareAsymptotic(20)
