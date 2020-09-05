N,M=map(int,input().split())
l=[list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if l[i][j]=='0':
            origin=(i,j,0)
def BFS(origin):
    level={origin:(0,0)}
    parent={origin:None}
    i=1
    frontier=[origin]
    while frontier:
        next=[]
        for row,col,key in frontier:
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nrow,ncol,nkey=row+dr,col+dc,key
                if not (0<=nrow<N and 0<=ncol<M):
                    continue
                c=l[nrow][ncol]
                if c.islower():
                    nkey=nkey | (1<<(ord(c)-ord('a')))
                elif c.isupper() and not nkey & (1<<(ord(c)-ord('A'))):
                    continue
                if l[nrow][ncol]=='1':
                    return i
                if (nrow,ncol,nkey) not in level and c!='#':
                    level[(nrow,ncol,nkey)]=i
                    parent[(nrow, ncol, nkey)] = (row,col,key)
                    next.append((nrow,ncol,nkey))
        frontier=next
        i=i+1
    return -1

print(BFS(origin))