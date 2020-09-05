def swap(n,direction):
    #0 up 1 right 2 down 3 left
    zero=0
    split=list(n)
    for i in range(9):
        if n[i]=="9":
            zero=i
            break
    if direction==0:
        if zero<3:
            return False
        split[zero],split[zero-3]=split[zero-3],split[zero]
        return "".join(split)
    elif direction==1:
        if zero%3==2:
            return False
        split[zero], split[zero +1] = split[zero +1], split[zero]
        return "".join(split)
    elif direction==2:
        if zero>5:
            return False
        split[zero], split[zero + 3] = split[zero + 3], split[zero]
        return "".join(split)
    else:
        if zero%3==0:
            return False
        split[zero], split[zero -1] = split[zero -1], split[zero]
        return "".join(split)

l=tuple(tuple(map(int,input().split())) for _ in range(3))
origin=0
for i in range(3):
    for j in range(3):
        if l[i][j]:
            origin=origin*10+l[i][j]
        else:
            origin = origin * 10 + 9
origin=str(origin)
destination="123456789"

def BFS(origin):
    if origin==destination:
        return 0
    level={origin:0}
    i=1
    frontier=[origin]
    while frontier:
        next=[]
        for u in frontier:
            for v in range(4):
                temp=swap(u,v)
                if temp==destination:
                    return i
                elif temp and temp not in level:
                    level[temp]=i
                    next.append(temp)
        frontier=next
        i=i+1
    return -1
print(BFS(origin))