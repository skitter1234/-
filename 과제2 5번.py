import numpy as np
from numpy import sin, cos

sin=sin(np.pi*2/9)
cos=cos(np.pi*2/9)
g=10
m1=10
m2=4
m3=5
m4=6

a=np.array([[1.0,0.0,0.0,m1],[-1.0,2.0,0.0,m2],[0.0,-1.0,1.0,m3],[0.0,0.0,-1.0,m4]])
b=np.array([[g*m1*(sin-0.25*cos)],[g*m2*(sin-0.3*cos)],[g*m3*(sin-0.2*cos)],[-g*m4*(sin-cos)]])
c=np.linalg.solve(a,b)

d='T1,2,3 은 각각 {}, {}, {}이고 가속도는 {} 이다.'.format(c[0,0],c[1,0],c[2,0],c[3,0])
print(d)