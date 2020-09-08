N,M,R=map(int,input().split())
l=[[*map(int,input().split())] for _ in range(N)]
def gen(xr,xc,yr,yc,R):
	z,q,cur=[],[],(xr-1,xc)
	while cur[0]<yr:cur=(cur[0]+1,cur[1]);z.append(cur);q.append(l[cur[0]][cur[1]])
	while cur[1] < yc: cur=(cur[0],cur[1]+1);z.append(cur);q.append(l[cur[0]][cur[1]])
	while cur[0] >xr: cur = (cur[0] - 1, cur[1]);z.append(cur);q.append(l[cur[0]][cur[1]])
	while cur[1] >xc+1: cur = (cur[0], cur[1]-1);z.append(cur);q.append(l[cur[0]][cur[1]])
	R=R%len(z)
	q=q[-R:]+q[:-R]
	cnt=0
	for r,c in z:
		l[r][c]=q[cnt]
		cnt+=1
for i in range(min(N,M)//2):
	gen(0+i,0+i,N-1-i,M-1-i,R)
for r in l:
	for c in r:
		print(c,end=" ")
	print()