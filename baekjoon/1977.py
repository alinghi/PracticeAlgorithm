M=int(input())
N=int(input())
i,j=1,1
while i*i<M:
    i+=1
while j*j<=N:
    j+=1
j=j-1
if i>j:
    print(-1)
else:
    print(sum(z*z for z in range(i,j+1)))
    print(i*i)