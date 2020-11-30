N=int(input())
l=[]
s=[]
ans=[]
def x():
    n = 1
    idx = 0
    for _ in range(N):
        l.append(int(input()))
    while idx<N:
        if len(s)>0 and s[-1]==l[idx]:
            s.pop()
            idx+=1
            ans.append("-")
        elif n<=l[idx]:
            while n<=l[idx]:
                s.append(n)
                n=n+1
                ans.append("+")
        else:
            return False
    return True
if x():
    for c in ans:
        print(c)
else:
    print("NO")