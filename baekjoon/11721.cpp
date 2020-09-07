#include <iostream>
using namespace std;
int main(void)
{
    char a;
    int b = 0;
    while (cin >> a)
    {
        cout << a;
        b++;
        if (b == 10)
        {
            b = 0;
            cout << endl;
        }
    }
}