#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    constexpr auto endl = "\n";
    int x, i;
    cin >> x;
    i = 2;
    while (x != 1)
    {
        if (x % i == 0)
        {
            cout << i << endl;
            x = x / i;
        }
        else
        {
            i++;
        }
    }
}