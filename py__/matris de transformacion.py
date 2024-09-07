m=int(input('Ingrese m'))
n=int(input('Ingrese n'))
c=1;j=1;k=1
for i in range(m*n):
    if j<=n:
        print(i+1,c)
        c=c+m
        j+=1
    if j>n:
        j=1
        k+=1
        c=k
