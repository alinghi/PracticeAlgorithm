#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    constexpr auto endl = "\n";
    int a, b, a1, b1, temp;
    cin >> a >> b;
    if (b > a) {
        temp = b;
        b = a;
        a = temp;
    }
    a1 = a;
    b1 = b;
    while (b1 != 0) {
        temp = a1 % b1;
        a1 = b1;
        b1 = temp;
    }
    cout << a1 << endl;
    cout << a * b / a1 << endl;
}