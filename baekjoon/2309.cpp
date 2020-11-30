#include <algorithm>
#include <iostream>
#pragma warning(disable : 4996)
using namespace std;
int main()
{
    int a[9];
    int sum = 0;
    for (int i = 0; i < 9; i++)
    {
        cin >> a[i];
        sum += a[i];
    }
    sort(a, a + 9);
    sum = sum - 100;
    int i = 0;
    int j = 0;
    for (i = 0; i < 8; i++)
    {
        for (j = i + 1; j < 9; j++)
        {
            if (a[i] + a[j] == sum)
            {
                for (int k = 0; k < 9; k++)
                {
                    if (k == i || k == j)
                        continue;
                    cout << a[k] << endl;
                }
                return 0;
            }
        }
    }
}