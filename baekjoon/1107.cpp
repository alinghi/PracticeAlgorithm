#include <iostream>
#include <algorithm>
using namespace std;
#pragma warning(disable : 4996)
bool broken[10] = {false};
int able(int n)
{
    if (!n)
    {
        return broken[0] ? 0 : 1;
    }
    int len = 0;
    while (n > 0)
    {
        if (broken[n % 10])
            return 0;
        len++;
        n = n / 10;
    }
    return len;
}
int main(void)
{
    int target;
    cin >> target;
    int disable;
    cin >> disable;
    int temp;
    for (int i = 0; i < disable; i++)
    {
        cin >> temp;
        broken[temp] = true;
    }
    int ans = abs(target - 100);
    int len = 0;
    for (int i = 0; i <= 1000000; i++)
    {
        if (len = able(i))
            ans = min(ans, abs(i - target) + len);
    }
    cout << ans;
    return 0;
}