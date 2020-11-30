#include <iostream>
#include <cstdio>
#include <deque>
#include <vector>
#include <map>
#pragma warning(disable : 4996)
using namespace std;
int N, M;
int board[100][100] = {0};
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};
int BFS(int row, int col)
{
    map<pair<int, int>, int> level;
    level.insert(make_pair(make_pair(row, col), 1));
    map<pair<int, int>, pair<int, int>> parent;
    parent.insert(make_pair(make_pair(row, col), make_pair(-1, -1)));
    int i = 1;
    deque<pair<int, int>> frontier;
    frontier.push_back(make_pair(row, col));
    while (frontier.size())
    {
        deque<pair<int, int>> next;
        for (deque<pair<int, int>>::iterator it = frontier.begin(); it != frontier.end(); it++)
        {
            int r = (*it).first;
            int c = (*it).second;
            for (int dir = 0; dir < 4; dir++)
            {
                int nrow = r + dr[dir];
                int ncol = c + dc[dir];
                if (nrow == N - 1 && ncol == M - 1)
                    return i;
                pair<int, int> temp = make_pair(nrow, ncol);
                if (0 <= nrow && nrow < N && 0 <= ncol && ncol < M && board[nrow][ncol] == 1 && level.find(temp) == level.end())
                {
                    level.insert(make_pair(temp, i));
                    parent.insert(make_pair(temp, *it));
                    next.push_back(temp);
                }
            }
        }
        frontier = next;
        i = i + 1;
    }
    return -1;
}
int main(void)
{
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            scanf("%1d", &board[i][j]);
        }
    }
    printf("%d", 1 + BFS(0, 0));
    return 0;
}