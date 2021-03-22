import numpy as np

a=np.array([[1.0,2.0,4.0],[3.0,8.0,14.0],[2.0,6.0,13.0]])
b=np.array([[3.0],[13.0],[4.0]])
x=np.zeros((3,1))

n=len(a)

for k in range(n-1,0,-1):
    for i in range(k-1,-1,-1):
        if a[i,k] != 0.0 :
            lam = a[i,k]/a[k,k]
            a[i,0:n] = a[i,0:n] - lam*a[k,0:n]
            b[i] = b[i] - lam*b[k]

for k in range(0,n):
    x[k] = ( b[k] - np.dot(a[k,0:k],x[0:k]) )/a[k,k]
print(x)
