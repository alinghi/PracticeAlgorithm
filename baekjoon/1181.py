N=int(input())
l=[input() for i in range(N)]
l=list(set(l))
l.sort(key=lambda x: (len(x),x))
for i in l:
	print(i)