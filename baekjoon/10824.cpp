#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
using namespace std;


int main(void)
{
    string a, b, c, d;
    cin >> a >> b >> c >> d;
    a = a + b;
    c = c + d;
    long long int result1, result2;
    result1 = stoll(a);
    result2 = stoll(c);
    cout << result1 + result2 << endl;
}