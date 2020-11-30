N=int(input())
d={1:1,2:2,3:3}
for _ in range(N):
    a,b=map(int,input().split())
    d[a],d[b]=d[b],d[a]
for k,v in d.items():
    if v==1:
        print(k)