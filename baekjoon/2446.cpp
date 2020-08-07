#include <iostream>
using namespace std;

int main(void)
{
    int a;
    int j;
    cin >> a;
    for (int i = a; i > 0; i--) {
        for (int x = 0; x < a - i; x++) cout << " ";
        for (int k = 0; k < 2 * i - 1; k++) cout << "*";
        cout << endl;
    }
    for (int i = 2; i <= a; i++) {
        for (int x = 0; x < a - i; x++) cout << " ";
        for (int k = 0; k < 2 * i - 1; k++) cout << "*";
        cout << endl;
    }
}