l=[list(input().split()) for _ in range(5)]
s=set()
di=[0,0,1,-1]
dj=[1,-1,0,0]
def DFS(z,i,j):
    if len(z)==6:
        s.add(z)
        return
    for k in range(4):
        ni,nj=i+di[k],j+dj[k]
        if 0<=ni<5 and 0<=nj<5:
            DFS(z+l[i][j],ni,nj)
for i in range(5):
    for j in range(5):
        DFS("",i,j)
print(len(s))