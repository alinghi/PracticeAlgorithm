N=int(input())
m=[list(map(int,input().split())) for _ in range(N)]
dR,dC=(-1,0,0,1),(0,-1,1,0)
#size, eat, row, col
fish=[2,0,0,0]
time=0
for i in range(N):
	for j in range(N):
		if m[i][j]==9:
			fish[2],fish[3]=i,j
			m[i][j]=0
visit=[[False]*N for _ in range(N)]
q=[[fish[2],fish[3],0]]
visit[fish[2]][fish[3]]=True
while q:
	q = sorted(q, key=lambda x: (x[2], x[0], x[1]))
	row,col,level=q.pop(0)
	if 0<m[row][col]<fish[0]:
		m[row][col],fish[1]=0,fish[1]+1
		if fish[1]==fish[0]:
			fish[0],fish[1]=fish[0]+1,0
		fish[2],fish[3]=row,col
		time=time+level
		level=0
		q=[]
		visit = [[False] * N for _ in range(N)]
		visit[fish[2]][fish[3]] = True
	for i in range(4):
		nr,nc,nl=row+dR[i],col+dC[i],level+1
		if 0<=nr<N and 0<=nc<N and m[nr][nc]<=fish[0] and visit[nr][nc]==False:
			q.append([nr,nc,nl])
			visit[nr][nc]=True
print(time)