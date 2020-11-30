l=[map(int,input().split()) for _ in range(4)]
z=[]
current=0
for a,b in l:
    current+=(b-a)
    z.append(current)
print(max(z))