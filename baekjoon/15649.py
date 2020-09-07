import itertools
N,M=map(int,input().split())
for c in itertools.permutations(range(1,N+1),M):
	for n in c:
		print(n,end=" ")
	print()