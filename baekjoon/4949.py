while True:
    s=input()
    if s==".":
        break
    stack=[]
    flag=True
    for ch in s:
        if ch=="(":
            stack.append("(")
        elif ch==")":
            if not (stack and stack[-1]=="("):
                flag=False
                break
            else:
                stack.pop()
        elif ch=="[":
            stack.append("[")
        elif ch=="]":
            if not (stack and stack[-1]=="["):
                flag=False
                break
            else:
                stack.pop()
    print("yes" if flag and not stack else "no")


