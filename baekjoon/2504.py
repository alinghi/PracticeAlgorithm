s=input()
l=list(s)
try:
    while l:
        z=[]
        for i in l:
            if i=="(" or i=="[":
                z.append(i)
            elif i==")":
                cnt=0
                n=0
                while True:
                    temp=z.pop()
                    if temp=="(":
                        break
                    else:
                        n+=temp
                    cnt+=1
                if not cnt:
                    n=1
                n=2*n
                z.append(n)
            elif i=="]":
                cnt=0
                n=0
                while True:
                    temp=z.pop()
                    if temp=="[":
                        break
                    else:
                        n+=temp
                    cnt+=1
                if not cnt:
                    n=1
                n=3*n
                z.append(n)
        break
    print(sum(z))
except:
    print(0)