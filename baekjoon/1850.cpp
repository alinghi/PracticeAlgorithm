#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    constexpr auto endl = "\n";
    unsigned long long a, b, temp;
    cin >> a >> b;
    if (a < b) {
        temp = b;
        b = a;
        a = temp;
    }
    while (b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    for (int i = 0; i < a; i++) {
        cout << 1;
    }
}