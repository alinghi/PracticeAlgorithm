N=int(input())
l=list(map(int,input().split()))
m=max(l)
m=100/m
aver=sum(l)/len(l)
aver=aver*m
print(aver)