#include <iostream>
using namespace std;

int main(void)
{
    int a;
    int j;
    cin >> a;
    for (int i = 1; i <= a; i++) {
        for (int j = 0; j < a - i; j++) cout << " ";
        for (int x = 0; x < i; x++) cout << "* ";
        cout << endl;
    }
}