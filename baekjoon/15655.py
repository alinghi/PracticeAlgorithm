import itertools
N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for c in itertools.combinations(range(N),r=M):
	for n in c:
		print(l[n],end=" ")
	print()