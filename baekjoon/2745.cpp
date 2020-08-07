#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    unsigned long long int n=0;
    int b;
    string x;
    cin >> x >> b;
    unsigned long long int k = 1;
    for (int i = 0; i < x.size(); i++) {
        if (x[x.size() - 1 - i] >= '0' && x[x.size() - 1 - i] <= '9') {
            n +=  ((x[x.size() - 1 - i] - '0')) * k;
        }
        else {
            n +=  ((x[x.size() - 1 - i] - 'A'+10)) * k;
        }
        k *= b;
    }
    cout << n << endl;
}