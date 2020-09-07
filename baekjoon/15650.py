import itertools
N,M=map(int,input().split())
for c in itertools.combinations(range(1,N+1),r=M):
	for n in c:
		print(n,end=" ")
	print()