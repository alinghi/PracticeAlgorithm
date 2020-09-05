#include <algorithm>
#include <stdio.h>
#include <vector>
using namespace std;
int main()
{
    int n, answer;
    answer = 0;
    scanf("%d", &n);
    vector<int> a(n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    sort(a.begin(), a.end());
    do {
        int temp = 0;
        for (int j = 0; j < n - 1; j++) temp += (a[j]-a[j+1]>0) ? (a[j] - a[j + 1]) : (a[j+1] - a[j]);
        if (temp > answer) answer = temp;
    } while (next_permutation(a.begin(), a.end()));
    printf("%d", answer);
    return 0;
}