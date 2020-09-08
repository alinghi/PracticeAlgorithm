import itertools
move=dict()
l=[0,0,0,0]
l[0]=[i for i in range(21)]+[32,32,32,32,32]
l[1]=[5,21,22,23,24,30,31,20]+[32,32,32,32,32]
l[2]=[10,28,29,24,30,31,20]+[32,32,32,32,32]
l[3]=[15,27,26,25,24,30,31,20]+[32,32,32,32,32]
for j in range(4):
    for i in range(len(l[j])-5):
        move[l[j][i]]=[l[j][i+1],l[j][i+2],l[j][i+3],l[j][i+4],l[j][i+5]]
#move[current position][dice-1] will return future position
score=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,26,27,28,22,24,30,35,0]
def simulator(dices,horses):
    horse_pos=[0,0,0,0]
    ans=0
    for turn in range(10):
        current_position=horse_pos[horses[turn]]
        if current_position==-1:
            return 0
        future_position=move[current_position][dices[turn]-1]
        if future_position in horse_pos:
            return 0
        if future_position==32:
            horse_pos[horses[turn]]=-1
        else:
            horse_pos[horses[turn]] = future_position
            ans+=score[future_position]
    return ans

dices=list(map(int,input().split()))
ans=max(map(lambda x:simulator(dices,x),(horses for horses in itertools.product([0,1,2,3],repeat=10))))
print(ans)