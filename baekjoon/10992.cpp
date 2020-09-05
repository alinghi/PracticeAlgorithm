#include <iostream>
using namespace std;

int main(void)
{
    int a;
    int j;
    int x;
    cin >> a;
    for (int i = 1; i <= a-1; i++) {
        for (x = a - i; x > 0; x--) cout << " ";
        cout << "*";
        for (x = 0; x < 2 * i - 3; x++) {
            cout << " ";
        }
        if (x > 0) cout << "*";
        cout << endl;
    }
    for (int z = 0; z < 2 * a - 1; z++) {
        cout << "*";
    }
}