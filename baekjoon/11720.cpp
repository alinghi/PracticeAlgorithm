#include <iostream>
using namespace std;
int main(void)
{
    int a;
    int ans = 0;
    char b;
    cin >> a;
    for (int i = 0; i < a; i++)
    {
        cin >> b;
        ans += (b - '0');
    }
    cout << ans << endl;
    return 0;
}