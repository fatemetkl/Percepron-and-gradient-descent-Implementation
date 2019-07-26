import matplotlib.pyplot as plt
import numpy as np

learning_rate=0.2



w=[[0.1,0.1],[0.1,0.1],[0.1,0.1],[0.1,0.1]]

wp=[0.1,0.1]

x=[
	[-2,1],
	[-2,-1],
    [-2,0],
	[-1,2],
	[-1,-2],
	[0,2],
	[0,-2],
	[1,2],
	[1,-2],
	[2,1],
	[2,-1],
    [2,0],
	[-1,0],
	[0,0],
	[1,0]
]
xp=[
	[-2,1],
	[-2,-1],
    [-2,0],
	[-1,2],
	[-1,-2],
	[0,2],
	[0,-2],
	[1,2],
	[1,-2],
	[2,1],
	[2,-1],
    [2,0],
	[-1,0],
	[0,0],
	[1,0],
    [3,0],
    [3,1],
    [3,-1],
    [4,0],
    [3,1.5]
]

y=[1,1,1,1,1,1,1,1,1,1,1,1
,0,0,0	
]

yp=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0]



def unit_step(v):
	if v >=0:
		return 1
	else:
		return 0
	
def perceptron(x, w,b):
    v = np.dot(w, x)+b
    y =unit_step(v)
    return y


def five_perc(x,w):
    r=0
    b=0
    for n in range(0,4) :
        r+=perceptron(x, w[n],b)		
    if(r==0):
        return 0
    else:
        return 1



def last_perc(x,wp):
    b=2.5
    return perceptron(x,wp,b)    


def final_decision(x):
  
    r=0
    for n in range(0,4) :
        r+=perceptron(x, w[n],0)	

    print(r)    	
    if(r==0):
        return 0
    elif(perceptron(x,wp,2.5)==0):
        return 0   

    else:
        return 1



for i in range(0,1):
     for j in range(0,len(x)-3):
         w = w + learning_rate*np.multiply(x[j],(y[j]-five_perc(x[j],w)))
     for j in range(0,len(xp)):
          wp = wp + learning_rate*np.multiply(xp[j],(yp[j]-last_perc(xp[j],wp)))

		

print("class 1 in cross and 0 is circule")
print("w is : ",w,wp)
print("input  0,0 in train set",final_decision([0,0]))	

print("input 0,-2 in train set",final_decision([-2,0]))	

print("input 0,-4 in test (class 1)",final_decision([2.54,0]))

print("input is 0, 1 in test set ",final_decision([4,0]))
