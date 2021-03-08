import numpy as np
import matplotlib.pyplot as plt
import scipy

ey=np.array([0,1])
for alpha in np.arange(-2,2,0.2):
    A=np.array([[1,alpha],[0,1]])
    v=np.dot(A,ey)
    plt.arrow(0,0,v[0],v[1],head_width=0.1,color='r')
plt.xlim(-2,2)
plt.ylim(0,2)
plt.show()