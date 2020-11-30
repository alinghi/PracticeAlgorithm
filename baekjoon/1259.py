while True:
    s=input()
    if s=="0":
        break
    else:
        print("yes" if s==s[::-1] else "no")
