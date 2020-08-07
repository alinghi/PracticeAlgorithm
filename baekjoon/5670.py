import sys
def ordd(x):
	return ord(x)-ord('a')
def ssum(x):
	ans=0
	for i in x:
		if i==None:
			continue
		else:
			ans+=1
	return ans
class Trie:
	def __init__(self,c):
		self.c=c
		self.nodelist=[None]*26
		self.terminal=False
	def insert(self, s):
		cur=self
		while True:
			index=ordd(s[0])
			if not cur.nodelist[index]:
				cur.nodelist[index]=Trie(index)
			if len(s)==1:
				cur.nodelist[index].terminal=True
				break
			cur=cur.nodelist[index]
			s=s[1:]
	def find(self,s):
		ans=0
		cnt=0
		cur=self
		while cnt<len(s):
			index=ordd(s[cnt])
			if cnt==0:
				cur=cur.nodelist[index]
				cnt+=1
				ans+=1
				continue
			if cur.terminal:
				cur = cur.nodelist[index]
				cnt += 1
				ans += 1
				continue
			z= ssum(cur.nodelist)
			cur=cur.nodelist[index]
			cnt+=1
			if z!=1:
				ans+=1
		return ans
def solution(n,l):
	x=Trie("")
	ans=0
	for i in l:
		x.insert(i)
	for i in l:
		ans+=x.find(i)
	print("{:0.2f}".format(round(ans/len(l),2)))

for line in sys.stdin:
	n=int(line)
	l=[input() for _ in range(n)]
	solution(n,l)