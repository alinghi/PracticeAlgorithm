import itertools
N,M=map(int,input().split())
for c in itertools.product(range(1,N+1),repeat=M):
	for n in c:
		print(n,end=" ")
	print()