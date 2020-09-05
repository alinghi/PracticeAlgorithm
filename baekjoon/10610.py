N=list(map(int,input()))
N=sorted(N)
if N[0]==0 and sum(N)%3==0:
	for i in range(len(N)):
		print(N[-i-1],end="")
else:
	print(-1)