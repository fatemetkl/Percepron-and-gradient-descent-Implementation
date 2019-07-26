import numpy as np

def unit_step(v):
	if v >= 0:
		return 1
	else:
		return 0
	
def perceptron(x, w, b):
    v = np.dot(w, x)+b
    y =unit_step(v)
    return y


def NOR_percep(x):
    w = np.array([-1, -1])
    b = 0.5
    result = perceptron(x, w, b)
    return result


example1 = np.array([1, 1])
example2 = np.array([1, 0])
example3 = np.array([0, 1])
example4 = np.array([0, 0])

print("1 NOR 1: ",NOR_percep(example1))
print("1 NOR 0: ",NOR_percep(example2))
print("0 NOR 1: ",NOR_percep(example3))
print("0 NOR 0: ",NOR_percep(example4 )) 