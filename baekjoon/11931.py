import sys
N=int(input())
l=[]
for _ in range(N):
    s = sys.stdin.readline()
    l.append(int(s))
l.sort(key=lambda x:-x)
for ch in l:
    print(ch)