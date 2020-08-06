N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(M)]
m=[[0]*N for _ in range(M)]
d={}
#1 west 2 north 4 east-> 8south
dr=[0,-1,0,1]
dc=[-1,0,1,0]
def DFS(row,col,cnt):
    if m[row][col]==0:
        m[row][col]=cnt
        d[cnt]+=1
        for i in range(4):
            if not (1<<i) & l[row][col]:
                DFS(row+dr[i],col+dc[i],cnt)
    else:
        return

cnt=1
room_number=0
largest_room=0
for r in range(M):
    for c in range(N):
        d[cnt]=0
        DFS(r,c,cnt)
        if d[cnt]>0:
            room_number+=1
            if largest_room<d[cnt]:
                largest_room=d[cnt]
        cnt+=1

superset=set()
ans=0
for r in range(M):
    for c in range(N):
        for i in range(4):
            if 0<=r+dr[i]<M and 0<=c+dc[i]<N:
                superset.add((m[r+dr[i]][c+dc[i]],m[r][c]))
for i in superset:
    if i[0]!=i[1]:
        ans=max(d[i[0]]+d[i[1]],ans)
print(room_number)
print(largest_room)
print(ans)