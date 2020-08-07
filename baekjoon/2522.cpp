#include <iostream>
using namespace std;

int main(void)
{
    int a;
    int j;
    cin >> a;
    for (int i = 1; i < a; i++) {
        for (int k = a - i; k > 0; k--) cout << " ";
        for (int j = 0; j < i; j++) cout << "*";
        cout << endl;
    }
    for (int i = a; i > 0; i--) {
        for (int k = a - i; k > 0; k--) cout << " ";
        for (int j = 0; j < i; j++) cout << "*";
        cout << endl;
    }
}