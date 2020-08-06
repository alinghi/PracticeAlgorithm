N=int(input())
l=[int(input()) for _ in range(N)]
l.sort(key=lambda x:-x)
ans=[]
for i in reversed(range(N)):
    ans.append((i+1)*l[-1])
    l.pop()
print(max(ans))
    