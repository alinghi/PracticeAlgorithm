import collections
N=input()
l=collections.Counter([ord(i)-ord('0') for i in N])
for i in reversed(range(10)):
	for j in range(l[i]):
		print(i,end="")
