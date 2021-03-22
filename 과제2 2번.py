import numpy as np

A=np.array([[0.0,0.0,2.0,1.0,2.0],[0.0,1.0,0.0,2.0,-1.0],[1.0,2.0,0.0,-2.0,0.0],[0.0,0.0,0.0,-1.0,1.0],[0.0,1.0,-1.0,1.0,-1.0]])
b=np.array([[1.0],[1.0],[-4.0],[-2.0],[-1.0]])
#A행렬에서 0이 k행, k열에 없도록 재배치
d=np.array([2,4,0,1,3])
A=A[d]                  #재배치한 A

x=np.zeros((5,1))

n=len(A)

for k in range(0,n-1):
    for i in range(k+1,n):
        if A[i,k] != 0.0 :
            lam = A[i,k]/A[k,k]
            A[i,k:n] = A[i,k:n] - lam*A[k,k:n]
            b[i] = b[i] - lam*b[k]

for k in range(n-1,-1,-1):
    x[k] = ( b[k] - np.dot(A[k,k+1:n],x[k+1:n]) )/A[k,k]


print(x)
c=np.linalg.solve(A,b)
print(c)

#혹은

A=np.array([[0.0,0.0,2.0,1.0,2.0],[0.0,1.0,0.0,2.0,-1.0],[1.0,2.0,0.0,-2.0,0.0],[0.0,0.0,0.0,-1.0,1.0],[0.0,1.0,-1.0,1.0,-1.0]])
b=np.array([[1.0],[1.0],[-4.0],[-2.0],[-1.0]])
#A행렬에서 0이 k행, k열에 없도록 재배치
d=np.array([2,4,0,1,3])
A=A[d]                  #재배치한 A

c=np.hstack([A,b])

n=len(c)

for k in range (0,n):
    c[k,k:n+1]=c[k,k:n+1]/c[k,k]
    for i in range (k+1,n):
        lam=c[i,k]              
        c[i,k:n+1]=c[i,k:n+1]-lam*c[k,k:n+1]

for k in range (0,n):
    for i in range(k+1,n):
        lam=c[n-1-i,n-1-k]
        c[n-1-i,n-1-k:n+1]=c[n-1-i,n-1-k:n+1]-lam*c[n-1-k,n-1-k:n+1]

print(c[0:n,n])         #가우시안 소거법으로 구한 해
H=np.linalg.solve(A,b)
print(H)