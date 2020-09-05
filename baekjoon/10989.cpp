#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
int main(void)
{
    constexpr auto endl = "\n";
    int n, temp;
    cin >> n;
    int p[10001] ={ 0 };
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp);
        p[temp]++;
    }

    for (int i = 0; i < 10001; i++) {
        for (int j = 0; j < p[i]; j++) {
            printf("%d\n", i);
        }
    }
    return 0;
}