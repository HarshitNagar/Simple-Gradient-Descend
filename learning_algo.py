import matplotlib.pyplot as plt
from numpy import *

ALPHA = 0.0007
M = 4
x = [2104, 1416, 1534, 852]
y = [460, 232, 315, 178]

#plt.plot(x,y,'ro')
#plt.show()

THETA0 = 2
THETA1 = 1

def sumA():
    ansA = 0
    for i in range(0,M):
        ansA += THETA0 + (THETA1 * x[i]) - y[i]
    return ansA

def sumB():
    ansB = 0
    for i in range(0,M):
        ansB += ( THETA0 + (THETA1 * x[i]) - y[i] ) * (x[i])
    return ansB


temp0 = THETA0 - ( ALPHA/M )*sumA()

temp1 = THETA1 - ( ALPHA/M )*sumB()

THETA0 = temp0
THETA1 = temp1

print(THETA0)
print("\n")
print(THETA1)
print("\n")


X = arange(800, 2200, 200)
Y = ( THETA0*X ) + THETA1
plt.plot(X,Y)
plt.plot(x,y,'ro')
plt.show()
