N = int(input())
l = [list(map(int,input().split())) for _ in range(N)]
def BFS(row, col, direction):
    if row == N-1 and col == N-1:
        return 1
    cnt = 0
    if direction == 0: # -
        if col+1 < N and l[row][col+1] == 0:
            cnt += BFS(row, col+1, 0)
        if row+1 < N and col+1 < N and l[row][col+1] == 0 and l[row+1][col] == 0 and l[row+1][col+1] == 0:
            cnt += BFS(row+1, col+1, 1)
    elif direction == 1: # dig
        if col+1 < N and l[row][col+1] == 0:
            cnt += BFS(row, col+1, 0)
        if row+1 < N and l[row+1][col] == 0:
            cnt += BFS(row+1, col, 2)
        if row+1 < N and col+1 < N and l[row][col+1] == 0 and l[row+1][col] == 0 and l[row+1][col+1] == 0:
            cnt += BFS(row+1, col+1, 1)
    elif direction == 2: # |
        if row+1 < N and l[row+1][col] == 0:
            cnt += BFS(row+1, col, 2)
        if row+1 < N and col+1 < N and l[row][col+1] == 0 and l[row+1][col] == 0 and l[row+1][col+1] == 0:
            cnt += BFS(row+1, col+1, 1)
    return cnt
print(BFS(0, 1, 0))