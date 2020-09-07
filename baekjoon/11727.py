N=int(input())
l=[0,1,3]
for i in range(3,N+1):
	l.append(l[-1]+2*l[-2])
print(l[N]%10007)