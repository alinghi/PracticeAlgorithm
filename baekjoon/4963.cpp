#include <iostream>
#include <cstdio>
#pragma warning(disable : 4996)
using namespace std;
int board[50][50] = {0};
int w, h;
int dr[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dc[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
void dfs(int row, int col)
{
    board[row][col] = 2;
    for (int dir = 0; dir < 8; dir++)
    {
        int nrow = row + dr[dir];
        int ncol = col + dc[dir];
        if (0 <= nrow && nrow < h && 0 <= ncol && ncol < w && board[nrow][ncol] == 1)
        {
            dfs(nrow, ncol);
        }
    }
    return;
}

int main(void)
{
    w = 1;
    while (true)
    {
        scanf("%d %d", &w, &h);
        if (w == 0 && h == 0)
            break;
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                scanf("%d", &board[i][j]);
            }
        }
        int cc = 0;
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                if (board[i][j] == 1)
                {
                    dfs(i, j);
                    cc++;
                }
            }
        }
        cout << cc << endl;
    }
    return 0;
}