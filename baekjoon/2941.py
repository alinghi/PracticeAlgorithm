s=input()
#lets do data abstraction
compares=[(3,"dz="),(2,"c="),(2,"c-"),(2,"d-"),(2,"lj"),(2,"nj"),(2,"s="),(2,"z=")]
i=0
cnt=0
while i<len(s):
    flag=False
    for compare in compares:
        if i+compare[0]<=len(s) and s[i:i+compare[0]]==compare[1]:
            cnt+=1
            i+=compare[0]
            flag=True
            break
    if not flag:
        cnt+=1
        i+=1

print(cnt)