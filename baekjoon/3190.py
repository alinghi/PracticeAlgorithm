import collections
import sys
def board_init(board_size):
    #include DUMMY for processing row and column in real order not starting by 0
    l=[[0]*(board_size+2) for _ in range(board_size+2)]
    number_of_apple=int(input())
    #0 represent movable area 1 represent apple 2 represe
    for i in range(number_of_apple):
        #row,column
        row, col=map(int, input().split())
        l[row][col]=1
    for i in range(board_size+2):
        l[i][0]=2
        l[0][i]=2
        l[board_size+1][i]=2
        l[i][board_size+1]=2
    return l

def op_init():
    number_of_op=int(input())
    dic={}
    for i in range(number_of_op):
        time, direction=input().split()
        dic[int(time)]=direction
    return dic

def print_board(board_map):
    for i in range(len(board_map)):
        print(board_map[i])

def print_map(de,board_size):
    l=[[0]*(board_size+2) for _ in range(board_size+2)]
    for i in range(board_size+2):
        l[i][0]=2
        l[0][i]=2
        l[board_size+1][i]=2
        l[i][board_size+1]=2
    for i in de:
        l[i[0]][i[1]]="*"
    for i in range(board_size+2):
        for j in range(board_size+2):
            print(l[i][j],end="")
        print()
    print("-----------------------------")


def rotation(direction, op):
    '''
    :param direction: right 0 down 1 left 2 up 3
    :param op: L left turn D right turn
    :return: return new direction
    '''
    if op=='D':
        return (direction+1) % 4
    elif op=='L':
        return (direction-1) % 4
    else:
        return -1

def extend(head,direction):
    #direction right 0 down 1 left 2 up 3
    if direction==0:
        return (head[0],head[1]+1)
    elif direction==1:
        return (head[0]+1,head[1])
    elif direction==2:
        return (head[0],head[1]-1)
    else:
        return (head[0]-1,head[1])



def solver():
    #INPUT
    board_size=int(input())
    board_map=board_init(board_size)
    op=op_init()
    de = collections.deque()
    de.append((1, 1))
    def isGameover(head):
        if board_map[head[0]][head[1]]==2:
            return True
        elif head in de:
            return True
        else:
            return False

    def simulator():
        gameover=False
        elapsed_time = 0
        direction=0

        #de[-1]->snake head
        #de[0]->snake tail
        while not gameover:
            #print_map(de, board_size)
            #Rotation
            if op.get(elapsed_time):
                direction=rotation(direction,op.get(elapsed_time))
            #Extend
            head=extend(de[-1],direction)
            gameover=isGameover(head)

            #apple determination
            if board_map[head[0]][head[1]]==1:
                # if apple tail stay
                board_map[head[0]][head[1]]=0
            else:
                #not apple - delete tail = pop left
                de.popleft()
            #if not game over extend
            de.append(head)
            elapsed_time=elapsed_time+1
        return elapsed_time
    ans=simulator()
    print(ans)

#sys.stdin=open("input.txt","r")
#sys.stdout=open("output.txt","w")
solver()