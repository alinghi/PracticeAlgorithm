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
    unsigned long long int a = 1;
    cin >> x;
    for (int i = 1; i <= x; i++) {
        a*= i;
    }
    cout << a;
}