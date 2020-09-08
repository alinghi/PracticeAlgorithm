import itertools
def rotate(l,r,c,s):
	r,c=r-1,c-1
	for i in range(1,s+1):
		temp1=l[r-i][c+i]
		temp2=l[r+i][c+i]
		temp3=l[r+i][c-i]
		#push right 2*i
		for j in range(2*i):
			l[r-i][c+i-j]=l[r-i][c+i-1-j]
		#push down 2*i-1
		for j in range(2*i-1):
			l[r+i-j][c+i]=l[r+i-1-j][c+i]
		l[r-i+1][c+i]=temp1
		#push left 2*i-1
		for j in range(2*i-1):
			l[r+i][c-i+j]=l[r+i][c-i+1+j]
		l[r+i][c+i-1]=temp2
		#push up 2*i
		for j in range(2*i-1):
			l[r-i+j][c-i]=l[r-i+1+j][c-i]
		l[r+i-1][c-i]=temp3
	return


N,M,K=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
rcs=[list(map(int,input().split())) for _ in range(K)]

ans = 987654321
for z in itertools.permutations(rcs):
	messy_l = [row[:] for row in l]
	for x in z:
		rotate(messy_l,x[0],x[1],x[2])
	for line in messy_l:
		ans=min(sum(line),ans)
print(ans)