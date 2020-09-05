#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <tuple>
using namespace std;


int main(void)
{
    constexpr auto endl = "\n";
    int n, k;
    scanf("%d %d", &n, &k);
    int *arr=new int[n];
    int num;
    for (int i=0;i<n;i++) {
        scanf("%d", &arr[i]);
    }
    sort(&arr[0], &arr[n]);
    printf("%d", arr[k-1]);

    return 0;
}
