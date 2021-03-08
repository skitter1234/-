def func(x,y):
    return x+y
a=lambda x,y:x+y
print(a(1,2))
print(func(1,2))

import numpy as np
import matplotlib.pyplot as plt
import scipy
from numpy import sin, cos, exp
print(sin(np.pi/2))

ex=np.array([1,0])
ey=np.array([0,1])
plt.arrow(0,0,ex[0],ex[1],head_width=0.2,color='b')
plt.arrow(0,0,ey[0],ey[1],head_width=0.2,color='r')
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()

u=np.array([1,1])
for alpha in np.arange(-1,1,0.2):
    A=np.array([[1,alpha],[0,alpha]])
    v=np.dot(A,u)

    plt.arrow(0,0,v[0],v[1],head_width=0.1,color='r')
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()

A=np.array([[1,1],[0,1]])
print(np.dot(A,ex))
print(np.dot(A,ey))

A=np.array([[1,2],[0,3]])
Ainv=np.linalg.inv(A)
b=np.array([5,4])
print(Ainv)
print(A)

print(np.dot(Ainv,b))

xsol=np.linalg.solve(A,b)
print('Sol',xsol)

t1=30
t2=90
a=t1**2/2
b=t2**2/2
u=np.array([[a,a],[b,-b]])
v=np.array([[100],[100]])
x=np.linalg.solve(u,v)
print(x)

t1=5
t2=15
u=np.array([[t1,t1],[t2,-t2]])
v=np.array([[100],[100]])
x=np.linalg.solve(u,v)
print(x)