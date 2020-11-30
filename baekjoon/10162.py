N=int(input())
d=lambda x:-1 if x%10>0 else (N//300,(N%300)//60,(N%60)//10)
if isinstance(d(N),tuple):
    for i in d(N):
        print(i,end=" ")
else:
    print(-1)