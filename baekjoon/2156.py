import sys
input = lambda: sys.stdin.readline().rstrip()
N=int(input())
l=[int(input()) for _ in range(N)]
if N<=2:
    print(sum(l))
else:
    v=(l[0],l[1],l[0]+l[1])
    for i in range(2,N): v=(max(v),v[0]+l[i],v[1]+l[i])
    print(max(v))