N=int(input())
l=list(map(int,input().split()))
l=sorted(l)
ans=0
time=0
for i in range(len(l)):
	time+=l[i]
	ans+=time
print(ans)