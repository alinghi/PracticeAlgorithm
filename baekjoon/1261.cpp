#include <iostream>
#include <cstdio>
#include <algorithm>
#include <deque>
#pragma warning(disable : 4996)
using namespace std;
int board[100][100] = {0};
int visited[100][100] = {-1};
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};
int main(void)
{
    int N, M;

    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            scanf("%1d", &board[i][j]);
            visited[i][j] = -1;
        }
    }
    deque<pair<int, int>> q;
    visited[0][0] = 0;
    q.push_back(make_pair(0, 0));
    while (q.size())
    {
        pair<int, int> front = q.front();
        q.pop_front();
        for (int dir = 0; dir < 4; dir++)
        {
            int nrow = front.first + dr[dir];
            int ncol = front.second + dc[dir];
            if (0 <= nrow && nrow < M && 0 <= ncol && ncol < N)
            {
                //visited?
                if (visited[nrow][ncol] == -1)
                {
                    if (board[nrow][ncol] == 0)
                    {
                        visited[nrow][ncol] = visited[front.first][front.second];
                        q.push_front(make_pair(nrow, ncol));
                    }
                    else
                    {
                        visited[nrow][ncol] = visited[front.first][front.second] + 1;
                        q.push_back(make_pair(nrow, ncol));
                    }
                }
            }
        }
    }
    cout << visited[M - 1][N - 1];
    return 0;
}