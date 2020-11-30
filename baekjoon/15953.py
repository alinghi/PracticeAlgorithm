c1=[(500,1),(300,2),(200,3),(50,4),(30,5),(10,6),(0,100)]
c2=[(512,1),(256,2),(128,4),(64,8),(32,16),(0,100)]
d1=[(0,0)]
d2=[(0,0)]
cnt=0
for c in c1:
    cnt+=c[1]
    d1.append((c[0],cnt))
cnt=0
for c in c2:
    cnt+=c[1]
    d2.append((c[0],cnt))
N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    gift=0
    for c in d1:
        if a<=c[1]:
            gift+=c[0]
            break
    for c in d2:
        if b<=c[1]:
            gift+=c[0]
            break
    print(gift*10000)