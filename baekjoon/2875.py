N,M,K=map(int,input().split())
team=min(N//2, M)
N-=(2*team)
M-=(team)
K=K-N-M
if K>0:
	team-=((K-1)//3+1)
print(team)