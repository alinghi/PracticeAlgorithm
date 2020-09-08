import itertools
import sys
input = sys.stdin.readline
final_inning=int(input())
stat=[list(map(int,input().split())) for _ in range(final_inning)]
orders=list(itertools.permutations([1,2,3,4,5,6,7,8],8))
ans=0
for i in orders:
	order=list(i[:3]) + [0] + list(i[3:])
	current_inning, out_count, score, tasoon,status,earn = 0, 0, 0, 0,0,0
	while True:
		x = stat[current_inning][order[tasoon]]
		if x == 0:
			out_count = out_count + 1
			if out_count == 3:
				current_inning,out_count, status  = current_inning + 1,0,0
				if current_inning==final_inning:
					break
		else:
			temp=(status<<x)+(1<<(x-1))
			status=temp%8
			earn=((temp & 8)>>3)+((temp & 16)>>4)+((temp & 32)>>5)+((temp & 64)>>6)
			score=score+earn
		tasoon = (tasoon + 1) % 9
	ans=max(ans,score)
print(ans)