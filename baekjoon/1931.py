N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
l=sorted(l,key=lambda x:(x[1],x[0]))
start=0
p=[]
for i in l:
	if i[0]>=start:
		p.append(i)
		start=i[1]
print(len(p))