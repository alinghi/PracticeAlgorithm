class Trie:
	def __init__(self,c):
		self.nodelist={}
		self.terminal=False
		self.c=c
	def insert(self,s):
		cur=self
		while len(s):
			if s[0] not in cur.nodelist: cur.nodelist[s[0]]=Trie(s[0])
			if len(s)==1:
				cur.nodelist[s[0]].terminal=True
			cur=cur.nodelist[s[0]]
			s=s[1:]
	def find(self,s):
		cur=self
		while len(s):
			if len(s)==1:
				return True
			else:
				if cur.nodelist[s[0]].terminal:
					return False
				cur=cur.nodelist[s[0]]
				s=s[1:]
def solution():
	n=int(input())
	z=Trie(-1)
	l=[input() for _ in range(n)]
	for i in range(n):
		z.insert(l[i])
	ans=True
	for i in range(n):
		if not z.find(l[i]):
			ans=False
			break
	if ans:
		print("YES")
	else:
		print("NO")

TC=int(input())
for _ in range(TC):
	solution()