r,c,k=map(int,input().split())
l=[[0]*101 for _ in range(101)]
l[1][0],l[2][0],l[3][0]=3,3,3
l[0][3],l[0][2],l[0][1]=3,3,3
l[0][0]=100
for i in range(3):l[i+1][1],l[i+1][2],l[i+1][3]=map(int,input().split())
def getRow(i):
    s=100
    return l[i][1:1+s]
def getCol(i):
    s=100
    ret=[l[k][i] for k in range(1,1+s)]
    return ret
def writeRow(i,given_list):
    given_list=given_list[:100]
    l[i][0]=len(given_list)
    for k in range(1,len(given_list)+1):
        l[i][k]=given_list[k-1]
    for k in range(len(given_list)+1,101):
        l[i][k]=0
    return
def writeCol(i,given_list):
    given_list = given_list[:100]
    l[0][i] = len(given_list)
    for k in range(1, len(given_list) + 1):
        l[k][i] = given_list[k - 1]
    for k in range(len(given_list)+1,101):
        l[k][i]=0
    return
def transform(given_list):
    d,dd,ddd={},[],[]
    for i in given_list:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for k in d.items():
        dd.append(k)
    dd.sort(key=lambda x:(x[1],x[0]))
    for k in dd:
        if k[0]!=0:
            ddd.append(k[0])
            ddd.append(k[1])
    return ddd
time=0
while l[r][c]!=k and time<=100:
    rr=max(getRow(0))
    cc=max(getCol(0))
    if rr>=cc:#r mode
        for i in range(1,101):
            t=getRow(i)
            t=transform(t)
            writeRow(i,t)
    else:#c mode
        for i in range(1,101):
            t=getCol(i)
            t=transform(t)
            writeCol(i,t)
    time+=1
if time==101:
    print(-1)
else:
    print(time)