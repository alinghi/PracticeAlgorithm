l=[("A",3),("D",3),("G",3),("J",3),("M",3),("P",4),("T",3),("W",4)]
dial={}
for idx,(ch,i) in enumerate(l):
    for j in range(i):
        dial[chr(ord(ch)+j)]=idx+3
print(sum(map(lambda x:dial[x],input())))