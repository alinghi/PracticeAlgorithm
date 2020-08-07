#include <iostream>
using namespace std;

int main(void)
{
    int a;
    int j;
    cin >> a;
    for (int i = 1; i < a; i++) {
        for (j = 0; j < i; j++) cout << "*";
        for (int k = 2 * a- 2*(j); k >0; k--) cout << " ";
        for (j = 0; j < i; j++) cout << "*";
        cout << endl;
    }
    for (int i = a; i > 0; i--) {
        for (j = 0; j < i; j++) cout << "*";
        for (int k = 2 * a - 2 * (j); k > 0; k--) cout << " ";
        for (j = 0; j < i; j++) cout << "*";
        cout << endl;
    }
}