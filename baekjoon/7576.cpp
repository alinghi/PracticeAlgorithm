#include <cstdio>
#include <map>
#include <deque>
#include <vector>
#pragma warning(disable : 4996)
using namespace std;
int board[1000][1000] = {0};
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};
int M, N; //M col N row
pair<int, int> BFS(deque<pair<int, int>> &frontier)
{
    int time = 1;
    int ret = 0;
    int ans = 0;
    while (frontier.size())
    {
        deque<pair<int, int>> next;
        ans += frontier.size();
        for (deque<pair<int, int>>::iterator u = frontier.begin(); u != frontier.end(); u++)
        {
            int row = (*u).first;
            int col = (*u).second;
            for (int dir = 0; dir < 4; dir++)
            {
                int nrow = row + dr[dir];
                int ncol = col + dc[dir];
                pair<int, int> nc = make_pair(nrow, ncol);
                if (0 <= nrow && nrow < N && 0 <= ncol && ncol < M && board[nrow][ncol] == 0)
                {
                    next.push_back(nc);
                    board[nrow][ncol] = time;
                    ret = time;
                }
            }
        }
        frontier = next;
        time++;
    }
    return make_pair(ret, ans);
}
int main(void)
{
    scanf("%d %d", &M, &N);
    int wall = 0;
    int temp;
    deque<pair<int, int>> frontier;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            scanf("%d", &temp);
            if (temp == -1)
                wall++;
            else if (temp == 1)
            {
                pair<int, int> coordinate = make_pair(i, j);
                frontier.push_back(coordinate);
            }
            board[i][j] = temp;
        }
    }
    pair<int, int> ret = BFS(frontier);
    printf("%d", N * M == ret.second + wall ? ret.first : -1);
    return 0;
}