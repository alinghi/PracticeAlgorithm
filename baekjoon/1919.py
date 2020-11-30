import collections
x1=collections.defaultdict(int)
x2=collections.defaultdict(int)
s1=input()
s2=input()
for s in s1:
    x1[s]=x1[s]+1
for s in s2:
    x2[s]=x2[s]+1
cnt=0
for c in list(map(chr, range(97, 123))):
    cnt+=abs(x1[c]-x2[c])
print(cnt)