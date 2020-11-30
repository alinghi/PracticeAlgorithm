n=int(input())
l=list(map(int,input().split()))
ans=0
cons=1
for i in l:
    if i:
        ans+=cons
        cons+=1
    else:
        cons=1
print(ans)