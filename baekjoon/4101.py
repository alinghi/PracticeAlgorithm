while True:
    a,b=map(int,input().split())
    if not (a or b):
        break
    print("Yes" if a>b else "No")