s=input()
ans=0
previous=-1
for i in s:
    if previous==-1:
        ans+=10
        previous=i
        continue
    if previous==i:
        ans+=5
        previous=i
    else:
        ans+=10
        previous=i
print(ans)