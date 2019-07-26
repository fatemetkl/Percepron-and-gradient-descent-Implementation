import random
import matplotlib.pyplot as plt
import numpy as np

alpha = 0.0001
threshold =150
w1 = random.randrange(1, 11) / 10
w2 = random.randrange(1, 11) / 10


def computeError(x, y, t):
    if (x * w1 + y * w2) >= threshold:
        activationFunction = 1
    else:
        activationFunction = 0
    e = t - activationFunction
    return e


with open('data.txt', 'r') as f:
    dataset = f.readlines()

train = []
Xs0 = []
Xs1 = []
Ys0 = []
Ys1 = []
for item in dataset:
    items = item.split(',')
    itemClass = items[2]

    if int(itemClass[0]) == 0:
        Xs0.append(float(items[0]))
    else:
        Xs1.append(float(items[0]))
    if int(itemClass[0]) == 0:
        Ys0.append(float(items[1]))
    else:
        Ys1.append(float(items[1]))

    train.append((float(items[0]), float(items[1]), int(itemClass[0])))

print(w1, w2)

for i in range(1000):
    for item in train:
        x = item[0]
        y = item[1]
        t = item[2]
        e = computeError(x, y, t)
        w1 = w1 + alpha * x * e
        w2 = w2 + alpha * y * e

print(w1, w2)

xx = np.linspace(-200, -50, 1000)
yy = (threshold/w2)- (xx*w1/w2)

plt.plot(Xs0, Ys0, 'ro', Xs1, Ys1, 'bo',xx, yy)
plt.show()

error=0
for item in train:

    x = item[0]
    y = item[1]
    t = item[2]
    if (x * w1 + y * w2) >= threshold:
        predict = 1
    else:
        predict = 0
    if predict == t:
        error=1+error


print (error/len(train))        

test = []
errorY = []
constRand1 = random.randrange(1, 51) / 10
constRand2 = random.randrange(1, 51) / 10
for i in range(100):
    w1 = constRand1
    w2 = constRand2
    test.append(train.pop())
    errorY.append(0)

    for j in range(10):
        for item in train:
            x = item[0]
            y = item[1]
            t = item[2]
            e = computeError(x, y, t)
            w1 = w1 + alpha * x * e
            w2 = w2 + alpha * y * e

    for item in test:
        x = item[0]
        y = item[1]
        t = item[2]
        if (x * w1 + y * w2) >= threshold:
            predict = 1
        else:
            predict = 0
        if predict != t:
            errorY[i] += 1

errorX = []
for i in range(100):
    errorX.append(100 - i)

plt.plot(errorX, errorY)
plt.show()