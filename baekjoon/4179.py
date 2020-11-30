def BFS():
    N, M=map(int,input().split())
    l=list(list(input()) for _ in range(N))
    J,F=None,[]
    dr=(0,0,1,-1)
    dc=(1,-1,0,0)
    for i in range(N):
        for j in range(M):
            if l[i][j]=="J":
                J=(i,j)
                l[i][j]="."
            if l[i][j]=="F":
                F.append((i,j))
    j_frontier=[J]
    j_parent={J:None}
    j_level={J:0}
    f_frontier=F
    i=1
    if F:
        while f_frontier:
            j_next=[]
            f_next=[]
            for u in f_frontier:
                for dir in range(4):
                    nr, nc = u[0] + dr[dir], u[1] + dc[dir]
                    if 0<=nr<N and 0<=nc<M and l[nr][nc]==".":
                        f_next.append((nr,nc))
                        l[nr][nc]="F"
            for u in j_frontier:
                for dir in range(4):
                    nr,nc=u[0]+dr[dir],u[1]+dc[dir]
                    if not (0<=nr<N and 0<=nc<M):
                        return i
                    if l[nr][nc]=="." and (nr,nc) not in j_level:
                        j_level[(nr,nc)]=i
                        j_parent[(nr,nc)]=u
                        j_next.append((nr,nc))


            f_frontier=f_next
            j_frontier=j_next
            i+=1
        return "IMPOSSIBLE"
    else:
        while j_frontier:
            j_next = []
            for u in j_frontier:
                for dir in range(4):
                    nr, nc = u[0] + dr[dir], u[1] + dc[dir]
                    if not (0 <= nr < N and 0 <= nc < M):
                        return i
                    if l[nr][nc] == "." and (nr, nc) not in j_level:
                        j_level[(nr, nc)] = i
                        j_parent[(nr, nc)] = u
                        j_next.append((nr, nc))
            j_frontier = j_next
            i += 1
        return "IMPOSSIBLE"




print(BFS())