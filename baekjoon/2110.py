K,N=map(int,input().split())
l=[int(input()) for _ in range(K)]
l.sort()
low=1
high=max(l)+1
while low+1<high:
	mid=(low+high)//2
	check=[min(l)]
	for i in l:
		if check[-1]+mid<=i:
			check.append(i)
	if len(check)>=N:
		low=mid
	else:
		high=mid
print(low)
