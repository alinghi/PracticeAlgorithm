N=int(input())
digits=[range(i,10) for i in range(10)]
l=[1]*10
p=10007
temp=[0]*10
for i in range(1,N):
    for j in range(10):
        temp[j]=0
        for k in digits[j]:
            temp[j]+=(l[k]%p)
    for j in range(10):
        l[j]=temp[j]%p
print(sum(l)%p)