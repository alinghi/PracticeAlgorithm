#include <iostream>
using namespace std;

int main(void)
{
    int a;
    cin >> a;
    for (int i = 0; i < a; i++) {
        for (int j = a-i; j > 0; j--) {
            cout << "*";
        }
        cout << endl;
    }
}