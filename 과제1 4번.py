#u+v=2ex, Au+Av=2Aex
#u-v=2ey, Au-Av=2Aey
import numpy as np
import matplotlib.pyplot as plt
import scipy

u=np.array([[1],[1]])
v=np.array([[1],[-1]])
b=np.array([[3],[2]])       #b=Au
c=np.array([[-1],[-2]])     #c=Av
d=b+c
e=b-c
f=np.array([[d[0,0],e[0,0]],[d[1,0],e[1,0]]])
g=np.array([[2,0],[0,2]])   #g는 u+v와 u-v를 붙여 2x2행렬로 만든 것, 2E와 같다.
A=f/2                       #f와 g의 역행렬을 곱하면 A가 나오는데 g가 단위행렬
print(A)