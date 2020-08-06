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
    int x;
    int a, b, temp;
    a = 0;
    b = 0;
    cin >> x;
    for (int i = 1; i <= x; i++) {
        temp = i;
        while (temp % 5 == 0) {
            a++;
            temp /= 5;
        }
        while (temp % 2 == 0) {
            b++;
            temp /= 2;
        }
    }
    if (a > b) cout << b << endl;
    else cout << a << endl;
}