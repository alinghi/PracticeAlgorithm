#include <algorithm>
#include <cstdio>
#include <vector>
#pragma warning(disable : 4996)
using namespace std;
int map[10][10];
long long distance(vector<int> &p)
{
    long long ans = 0;
    for (int i = 0; i < p.size() - 1; i++)
    {
        if (!map[p[i]][p[i + 1]])
            return 987654321;
        ans += map[p[i]][p[i + 1]];
    }
    if (!map[p[p.size() - 1]][p[0]])
        return 987654321;
    ans += map[p[p.size() - 1]][p[0]];
    return ans;
}

bool next_perm(vector<int> &p)
{
    int i = p.size() - 1;
    while (i > 0 && p[i - 1] >= p[i])
        i--;
    if (i <= 0)
        return false;
    int j = p.size() - 1;
    while (p[i - 1] >= p[j])
        j--;
    int temp = p[i - 1];
    p[i - 1] = p[j];
    p[j] = temp;
    reverse(p.begin() + i, p.end());
    return true;
}

int main(void)
{
    int N = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &map[i][j]);
        }
    }
    vector<int> dest;
    for (int i = 0; i < N; i++)
    {
        dest.push_back(i);
    }
    long long answer = 987654321;
    do
    {
        answer = min(answer, distance(dest));
    } while (next_perm(dest));
    printf("%lld", answer);
    return 0;
}