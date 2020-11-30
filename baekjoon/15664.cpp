#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#pragma warning(disable : 4996)
#pragma comment(linker, "/STACK:336777216")
using namespace std;
int N, M;

int main()
{
    cin >> N >> M;
    vector<int> v;
    int temp;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        v.push_back(temp);
    }
    int j = 0;
    sort(v.begin(), v.end());
    do
    {
        for (j = 0; j + 1 < M; j++)
            if (v[j] > v[j + 1])
                break;
        if (j + 1 >= M)
        {
            for (int i = 0; i < M; i++)
            {
                printf("%d ", v[i]);
            }
            puts("");
        }

        sort(v.begin() + M, v.begin() + N);
        reverse(v.begin() + M, v.begin() + N);
    } while (next_permutation(v.begin(), v.end()));
    return 0;
}