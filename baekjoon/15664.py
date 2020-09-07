import itertools
N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for c in sorted(list(set(itertools.combinations(l,M)))):
	for n in c:
		print(n,end=" ")
	print()