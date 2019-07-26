import matplotlib.pyplot as plt
import numpy as np

learning_rate=0.2
def unit_step(v):
	if v >= 0:
		return 1
	else:
		return 0
	
def perceptron(x, w):
    v = np.dot(w, x)
    y =unit_step(v)
    return y


def four_perc(x,w):
	r=0
	for n in range(0,4):
		r+=perceptron(x, w[n])		
	if(r==0):
		return 0
	else:
		return 1




w=[[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1]]

x=[
	[-2,1],
	[-2,-1],
	[-1,2],
	[-1,-2],
	[0,2],
	[0,-2],
	[1,2],
	[1,-2],
	[2,1],
	[2,-1],
	[-1,0],
	[0,0],
	[1,0]
]

y=[1,1,1,1,1,1,1,1,1,1
,0,0,0	
]

for i in range(0,10):
	for j in range(0,len(x)):
		w = w + learning_rate*np.multiply(x[j],(y[j]-four_perc(x[j],w)))



print("class 1 in cross and 0 is circule")
print("w is : ",w)
print("input  0,0 in train set : ",four_perc([0,0],w))	

print("input 0,-2 in train set: ",four_perc([0,-2],w))	

print("input 0,-4 in test (class 1) :",four_perc([0,-4],w))

print("input is 0, 1 in test set: ",four_perc([0,1],w))
print(four_perc([1,1],w))