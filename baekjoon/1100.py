l=[list(input()) for _ in range(8)]
even=lambda x:sum(1 if x[i]=='F' else 0 for i in range(0,8,2))
odd=lambda x:sum(1 if x[i]=='F' else 0 for i in range(1,8,2))
ans=0
for i in range(4):
    ans+=even(l[2*i])
    ans+=odd(l[2*i+1])
print(ans)