#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    constexpr auto endl = "\n";
    int limit = 1000000;

    vector<bool> sieve(limit+1, true);
    sieve[0] = false;
    sieve[1] = false;
    for (int i = 2; i * i <= limit; i++) {
        if (sieve[i]) {
            for (int j = (i*i); j <= limit; j+=i) {
                sieve[j] = false;
            }
        }
    }


    int input;
    while (true) {
        cin >> input;
        if (!input) break;
        for (int i = 3; i < input; i = i+2) {
            if (sieve[i] && sieve[input - i]) {
                cout << input << " = " << i << " + " << input - i << endl;
                break;
            }
        }
    }

}