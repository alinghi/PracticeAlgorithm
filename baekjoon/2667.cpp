#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#pragma warning(disable : 4996)
using namespace std;
int N;
int board[25][25] = {0};
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};
int dfs(int row, int col)
{
    board[row][col] = 2;
    bool flag = true;
    int count = 1;
    for (int dir = 0; dir < 4; dir++)
    {
        int nrow, ncol;
        nrow = row + dr[dir];
        ncol = col + dc[dir];
        if (0 <= nrow && nrow < N && 0 <= ncol && ncol < N && board[nrow][ncol] == 1)
        {
            flag = false;
            count += dfs(nrow, ncol);
        }
    }
    if (flag)
        return 1;
    return count;
}
int main(void)
{
    int i, j;
    vector<int> ans;
    cin >> N;
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            scanf("%1d", &board[i][j]);
        }
    }
    int cc = 0;
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            if (board[i][j] == 1)
            {
                ans.push_back(dfs(i, j));
                cc++;
            }
        }
    }
    cout << cc << endl;
    sort(ans.begin(), ans.end());
    for (vector<int>::iterator it = ans.begin(); it != ans.end(); it++)
    {
        cout << *it << endl;
    }
    return 0;
}