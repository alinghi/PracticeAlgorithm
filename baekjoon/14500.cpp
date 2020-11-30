#include <cstdio>
#include <algorithm>
#pragma warning(disable : 4996)
using namespace std;
int board[500][500];
//dr,dc
int tetro[19][3][2] =
    {
        {{0, 1}, {0, 2}, {0, 3}},   //-
        {{1, 0}, {2, 0}, {3, 0}},   //|
        {{0, 1}, {1, 0}, {1, 1}},   //.
        {{1, 0}, {2, 0}, {2, 1}},   //4
        {{1, 0}, {2, 0}, {2, -1}},  //5
        {{0, 1}, {1, 1}, {2, 1}},   //6
        {{0, 1}, {1, 0}, {2, 0}},   //7
        {{0, 1}, {0, 2}, {1, 0}},   //8
        {{0, 1}, {0, 2}, {1, 2}},   //9
        {{1, 0}, {1, 1}, {1, 2}},   //10
        {{1, 0}, {1, -1}, {1, -2}}, //11
        {{1, 0}, {1, 1}, {2, 1}},   //12
        {{1, 0}, {1, -1}, {2, -1}}, //13
        {{0, 1}, {-1, 1}, {-1, 2}}, //14
        {{0, 1}, {1, 1}, {1, 2}},   //15
        {{0, 1}, {0, 2}, {-1, 1}},  //16
        {{0, 1}, {0, 2}, {1, 1}},   //17
        {{1, 0}, {2, 0}, {1, -1}},  //18
        {{1, 0}, {2, 0}, {1, 1}}    //19
};

int main()
{
    int N, M;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            scanf("%d", &board[i][j]);
        }
    }
    int ans = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            for (int k = 0; k < 19; k++)
            {
                bool ok = true;
                int sum = board[i][j];
                for (int l = 0; l < 3; l++)
                {
                    int row = i + tetro[k][l][0];
                    int col = j + tetro[k][l][1];
                    if (0 <= row && row < N && 0 <= col && col < M)
                    {
                        sum += board[row][col];
                    }
                    else
                    {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                {
                    ans = max(ans, sum);
                }
            }
        }
    }
    printf("%d", ans);
    return 0;
}