class cube:
    clockwise=(6,3,0,7,4,1,8,5,2)
    direc=["U","F","D","L","R","B"]
    rotate12=dict()
    rotate12["U"]=[("B",2),("B",1),("B",0),("R",2),("R",1),("R",0),("F",2),("F",1),("F",0),("L",2),("L",1),("L",0)]
    rotate12["D"]=[("F",6),("F",7),("F",8),("R",6),("R",7),("R",8),("B",6),("B",7),("B",8),("L",6),("L",7),("L",8)]
    rotate12["F"] = [("U", 6), ("U", 7), ("U", 8), ("R", 0), ("R", 3), ("R", 6), ("D", 2), ("D", 1), ("D", 0), ("L", 8),
                     ("L", 5), ("L", 2)]
    rotate12["B"] = [("U", 2), ("U", 1), ("U", 0), ("L", 0), ("L", 3), ("L", 6), ("D", 6), ("D", 7), ("D", 8), ("R", 8),
                     ("R", 5), ("R", 2)]
    rotate12["L"] = [("U", 0), ("U", 3), ("U", 6), ("F", 0), ("F", 3), ("F", 6), ("D", 0), ("D", 3), ("D", 6), ("B", 8),
                     ("B", 5), ("B", 2)]
    rotate12["R"] = [("U", 8), ("U", 5), ("U", 2), ("B", 0), ("B", 3), ("B", 6), ("D", 8), ("D", 5), ("D", 2), ("F", 8),
                     ("F", 5), ("F", 2)]
    rotate15 = dict()
    #12<=15
    for d in direc:
        rotate15[d]=rotate12[d][9:]+rotate12[d][:9]

    def __init__(self):
        self.Cube=dict()
        self.Cube["U"]=["w"]*9
        self.Cube["D"]=["y"]*9
        self.Cube["F"]=["r"]*9
        self.Cube["B"]=["o"]*9
        self.Cube["L"]=["g"]*9
        self.Cube["R"]=["b"]*9
    def rotate(self,where):
        l=[]
        for i in range(9):
            l.append(self.Cube[where][cube.clockwise[i]])
        self.Cube[where]=l
        temp=[self.Cube[c][p] for c,p in cube.rotate15[where]]
        for i in range(12):
            self.Cube[cube.rotate12[where][i][0]][cube.rotate12[where][i][1]]  =temp[i]


N=int(input())
for _ in range(N):
    m=int(input())
    orders=input().split()
    exp=cube()
    for order in orders:
        if order[1]=="+":
            exp.rotate(order[0])
        else:
            exp.rotate(order[0])
            exp.rotate(order[0])
            exp.rotate(order[0])
        """
        print("-------------------")
        print(order)
        for d in cube.direc:
            print(d,exp.Cube[d])
        """
    for i in range(9):
        print(exp.Cube["U"][i],end="")
        if i%3==2:
            print()