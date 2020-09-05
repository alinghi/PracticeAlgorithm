import itertools
N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
ans=9e9
for i in itertools.permutations(range(N)):
	t=list(i)+[i[0]]
	dist=0
	for j in range(N):
		if l[t[j]][t[j+1]]==0:
			dist+=9e9
		dist+=l[t[j]][t[j+1]]
	ans=min(ans,dist)
print(ans)