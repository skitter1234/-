import numpy as np

#1
def backwdsub(A,b):
    n=len(b)
    for k in range(n-1,-1,-1):
        b[k]=(b[k]-np.dot(A[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

#2

#2-1
#정답 : x1=1, x2=x1, x3=x1+x2, x4=x2+x3, x5=x3+x4

#2-2
a1=np.eye(10)
a2=np.eye(10,k=-1)
a3=np.eye(10,k=-2)
A=a1-a2-a3
B=np.zeros((10,1))
B[0]=1
b=B

#2-3
#Ax=b
x=np.zeros((10,1))
n=len(A)
for k in range(0,n):
    x[k] = ( b[k] - np.dot(A[k,0:k],x[0:k]) )/A[k,k]

#3-1
A=np.array([[0.95,0.02],[0.05,0.98]])

#3-2
a=A
l=np.eye(2)
n=len(A)
l[1,0]=A[1,0]/A[0,0]
L=l
u=A
u[1,0]=0
u[1,1]=A[1,1]-L[1,0]*A[0,1]
U=u
print(np.dot(L,U))