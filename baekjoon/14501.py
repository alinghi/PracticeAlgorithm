def init(n):
    l=[list(map(int,input().split())) for _ in range(n)]
    l.insert(0,[])
    x=[]
    possibility=[True for _ in range(n+1)]
    possibility[0]=False
    for i in range(n):
        if (i+1)+l[i+1][0]-1>n:
            possibility[i+1]=False
    count=0
    for i in possibility:
        if i:
            x.append(count)
        count=count+1
    return l,possibility,x

def solver():
    n=int(input())
    l,possibility,x=init(n)
    def resign(day,aList):
        if day==n+1:
            for i in aList:
                if possibility[i]==False:
                    return -1

            temp=[True for _ in range(n+1)]
            for i in aList:
                for j in range(l[i][0]):
                    if temp[j+i]==False:
                        return -1
                    else:
                        temp[j+i]=False
            ans=0
            for i in aList:
                ans=ans+l[i][1]
            return ans
        ret=resign(day+1,aList)
        aList.append(day)
        ret=max(ret,resign(day+1,aList))
        aList.pop()
        return ret
    y=[]
    print(resign(0,y))
solver()