import itertools
N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for c in itertools.product(range(N),repeat=M):
	for n in c:
		print(l[n],end=" ")
	print()