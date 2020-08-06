def indicator(s):
	prev,l="0",[0]*26
	for c in s:
		if prev!=c:
			prev=c
			l[ord(c)-ord('a')]+=1
	ans=True
	for i in range(26):
		if l[i]>1:
			ans=False
	return ans
N=int(input())
print(sum(indicator(input()) for _ in range(N)))
