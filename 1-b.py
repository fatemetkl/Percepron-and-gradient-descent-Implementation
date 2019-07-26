import matplotlib.pyplot as plt
import numpy as np

learning_rate=0.1
def unit_step(v):
	if v >= 0:
		return 1
	else:
		return 0
	
def perceptron(x, w,b):
    v = np.dot(w, x)+b
    y =unit_step(v)
    return y


def NOR_percep(x,w,b):
    result = perceptron(x, w,b)
    return result





#random initialize

w = [0.2,0.1]
b=0.1
x=[[1.0,1.0],[1.0,0.0],[0.0,1.0],[0.0,0.0]]
y=[0.0,0.0,0.0,1.0]

for i in range(0,3):
    for j in range (0,len(x)):#one iteration
        #it is given from gradient descent formula 
        w[0] = w[0] + learning_rate*np.multiply(x[j][0],(y[j]-NOR_percep(x[j],w,b)))
        w[1] = w[1] + learning_rate*np.multiply(x[j][1],(y[j]-NOR_percep(x[j],w,b)))
        b=b+ learning_rate*(y[j]- NOR_percep(x[j],w,b))
      


print(" w after 3 epochs is : ",w)

example1 = np.array([1, 1])
example2 = np.array([1, 0])
example3 = np.array([0, 1])
example4 = np.array([0, 0])

print("1 NOR 1: ",NOR_percep(example1,w,b))
print("1 NOR 0: ",NOR_percep(example2,w,b))
print("0 NOR 1: ",NOR_percep(example3,w,b))
print("0 NOR 0: ",NOR_percep(example4,w,b)) 