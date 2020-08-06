N=int(input())
l=dict()
l[0]=0
l[1]=0
l[2]=1
l[3]=1
l[4]=2
l[5]=3
z=6
while z<=N+1:
    #0 s 2 3
    l[z]=min(l[z-1]+1,l[z//2]+1,l[z//3]+1)
    z+=1
    #1 s
    l[z] =l[z-1]+1
    z+=1
    #2 s 2
    l[z] =min(l[z - 1] + 1, l[z // 2] + 1)
    z += 1
    #3 s 3
    l[z] =min(l[z-1]+1,l[z//3]+1)
    z+=1
    #4 s 2
    l[z] =min(l[z - 1] + 1, l[z // 2] + 1)
    z += 1
    #5 s
    l[z] =l[z - 1] + 1
    z += 1
print(l[N])