l=[input() for _ in range(5)]
t=len(max(l,key=lambda x:len(x)))
def padding(s,t):
    if len(s)==t:
        return s
    i=t-(len(s))
    return s+"-"*i
l=[padding(s,t) for s in l]
ans=""
for j in range(t):
    for i in range(5):
        ans+="" if l[i][j]=="-" else l[i][j]
print(ans)