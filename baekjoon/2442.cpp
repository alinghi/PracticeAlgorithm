#include <iostream>
using namespace std;

int main(void)
{
    int a;
    cin >> a;
    for (int i = 0; i < a; i++) {
        for (int j = a-i-1; j >0; j--) {
            cout << " ";
        }
        for (int j =0; j < 2*i+1; j++) {
            cout << "*";
        }

        cout << endl;
    }
}