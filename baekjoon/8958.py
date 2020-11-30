N=int(input())
x=lambda s,cons,score:print(score) if not len(s) else x(s[1:],cons+1,score+cons+1) if s[0]=="O" else x(s[1:],0,score+0)
tuple(map(x,list(input() for _ in range(N)),(0,)*N,(0,)*N))