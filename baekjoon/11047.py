def solution(cost,coin):
	ans=0
	for i in range(len(coin)-1,-1,-1):
		if coin[i]<=cost:
			ans+=cost//coin[i]
			cost=cost%coin[i]
	return ans

N, cost=map(int,input().split())
coin=[int(input()) for i in range(N)]
print(solution(cost,coin))
