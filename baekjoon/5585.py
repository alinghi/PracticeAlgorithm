N=int(input())
l=[500,100,50,10,5,1]
N=1000-N
ans=0
for coin in l:
    if N>=coin:
        ans+=N//coin
        N=N%coin
print(ans)