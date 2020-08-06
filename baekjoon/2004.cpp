#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;
long long min(long long a, long long b) {
    if (a > b) return b;
    else return a;
}
long long count_five(int n) {
    long long ret = 0;
    for (long long i = 5; i <= n; i *= 5) {
        ret += n / i;
    }
    return ret;
}
long long count_two(int n) {
    long long ret = 0;
    for (long long i = 2; i <= n; i *= 2) {
        ret += n / i;
    }
    return ret;
}
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    constexpr auto endl = "\n";
    int n, m;
    cin >> n>> m;
    long long five, two;
    five = count_five(n) - count_five(m) - count_five(n - m);
    two = count_two(n) - count_two(m) - count_two(n - m);
    cout << min(five, two) << endl;
}