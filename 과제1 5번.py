import numpy as np
import matplotlib.pyplot as plt
import scipy

#토끼다리 4개, 닭다리 2개, 머리1개
#토끼 x마리, 닭 y마리
#4x+2y=92, x+y=40
A=np.array([[4,2],[1,1]])
u=np.array([[92],[40]])
v=np.linalg.solve(A,u)
b='토끼는 {}마리, 닭은 {}마리다.'.format(int(v[0,0]),int(v[1,0]))
print(b)