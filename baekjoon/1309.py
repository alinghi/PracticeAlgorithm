N=int(input())
l=[(0,0,0),(1,1,1)]
for i in range(2,N+1):
    left,right,blank=l[-1]
    l.append(((right+blank)%9901,(left+blank)%9901,(left+right+blank)%9901))
print(sum(l[-1])%9901)