s=input()
flag=False
stack=[]
ans=0
for ch in s:
    if ch=="(":
        flag=True
        stack.append("(")
    else:
        if flag:
            flag=False
            stack.pop()
            ans+=len(stack)
        else:
            ans+=1
            stack.pop()
print(ans)