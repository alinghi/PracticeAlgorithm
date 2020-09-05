N=int(input())
l=[0,1,2,4]
for i in range(11):
	l.append(l[-1]+l[-2]+l[-3])
for _ in range(N):
	print(l[int(input())])