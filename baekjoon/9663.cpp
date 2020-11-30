#include <iostream>
using namespace std;
int n;
int col[80] = {0};
int diag1[80] = {0};
int diag2[80] = {0};
int cnt;
void search(int y)
{
    if (y == n)
    {
        cnt++;
        return;
    }
    for (int x = 0; x < n; x++)
    {
        if (!col[x] && !diag1[x + y] && !diag2[x - y + n - 1])
        {
            col[x] = diag1[x + y] = diag2[x - y + n - 1] = 1;
            search(y + 1);
            col[x] = diag1[x + y] = diag2[x - y + n - 1] = 0;
        }
    }
}
int main(void)
{
    for (int i = 0; i < 80; i++)
    {
        col[i] = 0;
        diag1[i] = 0;
        diag2[i] = 0;
    }
    cin >> n;
    search(0);
    cout << cnt;
    return 0;
}