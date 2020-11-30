#include <iostream>
#include <vector>
using namespace std;

const int GREEN = 0;
const int BLUE = 1;
const int dy[] = {-1, 0};
const int dx[] = {0, 1};
int map[2][10][4];
int n;
int score = 0;

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}
void move_one_block(int color, int y, int x, int num)
{
    bool flag = false;
    map[color][y][x] = 0;
    while (y < 10)
    {
        if (map[color][y][x])
        {
            break;
        }
        flag = true;
        y++;
    }
    y--;
    map[color][y][x] = num;
}
void move_garo_block(int color, int y, int x, int num)
{
    bool flag = false;
    map[color][y][x] = 0;
    map[color][y][x + 1] = 0;
    while (y < 10)
    {
        if (map[color][y][x] || map[color][y][x + 1])
        {
            break;
        }
        flag = true;
        y++;
    }
    y--;
    map[color][y][x] = num;
    map[color][y][x + 1] = num;
}
void move_sero_block(int color, int y, int x, int num)
{
    bool flag = false;
    map[color][y + 1][x] = 0;
    map[color][y][x] = 0;
    while (y < 9)
    {
        if (map[color][y + 1][x])
        {
            break;
        }
        flag = true;
        y++;
    }
    y--;
    map[color][y][x] = num;
    map[color][y + 1][x] = num;
}
void down(int row, int color)
{
    // 요놈이 문제.....
    for (int y = row; y >= 4; y--)
    {
        for (int x = 0; x < 4; x++)
        {
            if (map[color][y][x] == 0)
                continue;
            bool move_flag = false;

            for (int dir = 0; dir < 2; dir++)
            {
                int ny = y + dy[dir], nx = x + dx[dir];
                if (ny < 4 || nx >= 4)
                    continue;

                int block_num = map[color][ny][nx];
                if (map[color][y][x] == block_num)
                {
                    move_flag = true;
                    if (dir == 0)
                    {
                        move_sero_block(color, ny, nx, block_num);
                        break;
                    }
                    else if (dir == 1)
                    {
                        move_garo_block(color, y, x, block_num);
                        break;
                    }
                }
            }
            if (move_flag)
                continue;
            move_one_block(color, y, x, map[color][y][x]);
        }
    }
}
void blur_delete(int color)
{
    int k = 0;
    for (int i = 5; i >= 4; i--)
    {
        for (int j = 0; j < 4; j++)
        {
            if (map[color][i][j] && i == 4)
            {
                k = 2;
                break;
            }
            else if (map[color][i][j] && i == 5)
            {
                k = 1;
                break;
            }
        }
    }
    if (k == 0)
        return;
    for (int i = 9; i >= 6; i--)
    {
        for (int j = 0; j < 4; j++)
        {
            map[color][i][j] = map[color][i - k][j];
            map[color][i - k][j] = 0;
        }
    }
}
void line_delete(int color)
{
    int delete_flag = 0;
    for (int i = 6; i <= 9; i++)
    {
        int cnt = 0;
        for (int j = 0; j < 4; j++)
        {
            if (map[color][i][j])
                cnt++;
        }
        if (cnt == 4)
        {
            for (int j = 0; j < 4; j++)
            {
                map[color][i][j] = 0;
            }

            score++;
            delete_flag = 1;
            down(i - 1, color);
        }
    }
    if (delete_flag)
        line_delete(color);
}
void put(int color, int t, int y, int x, int num)
{
    if (t == 1)
    {
        move_one_block(color, y, x, num);
    }
    else if ((t == 2 && color == GREEN) || (t == 3 && color == BLUE))
    {
        move_garo_block(color, y, x, num);
    }

    else if ((t == 3 && color == GREEN) || (t == 2 && color == BLUE))
    {
        move_sero_block(color, y, x, num);
    }
    line_delete(color);
    blur_delete(color);
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int t, y, x;
        cin >> t >> y >> x;

        put(GREEN, t, y, x, i + 1);
        put(BLUE, t, x, y, i + 1);
    }
    int cnt = 0;
    for (int color = 0; color < 2; color++)
    {
        for (int i = 6; i < 10; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (map[color][i][j])
                    cnt++;
            }
        }
    }
    cout << score << '\n'
         << cnt;
}