#include <iostream>
#include <vector>
#include <cstdio>
#pragma warning(disable : 4996)
using namespace std;
int N, M;
vector<int> V;
bool check[9];
void go(int prev)
{
    if (V.size() == M)
    {
        for (vector<int>::iterator it = V.begin(); it != V.end(); ++it)
        {
            printf("%d ", *it);
        }
        puts("");
        return;
    }
    for (int i = prev + 1; i <= N; i++)
    {
        if (check[i])
            continue;
        check[i] = true;
        V.push_back(i);
        go(i);
        check[i] = false;
        V.pop_back();
    }
    return;
}

int main(void)
{
    cin >> N >> M;
    go(0);
    return 0;
}