import numpy as np
import matplotlib.pyplot as plt
import scipy
from numpy import sin,cos

#1
A=np.eye(1000,dtype=int)
print(A)

#2
A=np.array([[1,2],[1,-3]])
B=np.array([[10],[5]])
C=np.linalg.solve(A,B)
D='x={},y={}'.format(C[0,0],C[1,0])
print(D)

#3
A=np.array([[1,2,1,0,0],[2,-1,3,0,0],[2,0,0,-1,-2],[0,2,0,-2,1],[0,0,2,-1,3]])
B=np.array([[5],[7],[4],[2],[0]])
C=np.linalg.solve(A,B)
D='s={},p={},d={},f={},g={}'.format(C[0,0],C[1,0],C[2,0],C[3,0],C[4,0])
print(D)

#4
A=np.array([[cos(np.pi*(1/9)),-sin(np.pi*(1/9))],[sin(np.pi*(1/9)),cos(np.pi*(1/9))]])
B=np.array([1,0])
C=np.dot(A,B)
print(C)

#5
A=np.array([[2.46,0.00,0.00],[-1.23,2.14,0.00],[0.00,0.00,10.00]])
B=np.array([[1,0,0],[0,1,0],[0,0,1]])
C=np.linalg.solve(A,B)
v1=([C[0,0],C[1,0],C[2,0]])
v2=([C[0,1],C[1,1],C[2,1]])
v3=([C[0,2],C[1,2],C[2,2]])
print(v1)
print(v2)
print(v3)