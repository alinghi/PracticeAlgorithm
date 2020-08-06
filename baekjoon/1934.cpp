#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    constexpr auto endl = "\n";
    int a, b, a1, b1, temp, n;
    cin >> n;
    for (int i = 0; i < n; i++) {
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
        cout << a * b / a1 << endl;
    }

}