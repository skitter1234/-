import numpy as np

a=np.array([[1,2,4],[3,8,14],[2,6,13]])
b=np.array([[3],[13],[4]])
x=np.zeros((3,1))

n=len(a)

for k in range(0,n-1):
    for i in range(k+1,n):
        if a[i,k] != 0.0 :
            lam = a[i,k]/a[k,k]
            a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
            b[i] = b[i] - lam*b[k]

for k in range(n-1,-1,-1):
    x[k] = ( b[k] - np.dot(a[k,k+1:n],x[k+1:n]) )/a[k,k]


print(x)
c=np.linalg.solve(a,b)
print(c)

#혹은

a=np.array([[1,2,4],[3,8,14],[2,6,13]])
b=np.array([[3],[13],[4]])
c=np.hstack([a,b])

n=len(c)

for k in range (0,n):
    c[k,k:n+1]=c[k,k:n+1]/c[k,k]
    for i in range (k+1,n):
        lam=c[i,k]              #c[k,k]=1 이므로
        c[i,k:n+1]=c[i,k:n+1]-lam*c[k,k:n+1]

for k in range (0,n):
    for i in range(k+1,n):
        lam=c[n-1-i,n-1-k]
        c[n-1-i,n-1-k:n+1]=c[n-1-i,n-1-k:n+1]-lam*c[n-1-k,n-1-k:n+1]

d=c[0:n,n]              #가우시안 소거법으로 구한 해
x=np.linalg.solve(a,b)
print(d)
print(x)

