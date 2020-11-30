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
    for (int i = prev; i <= N; i++)
    {
        V.push_back(i);
        go(i);
        V.pop_back();
    }
}

int main(void)
{
    cin >> N >> M;
    go(1);
    return 0;
}