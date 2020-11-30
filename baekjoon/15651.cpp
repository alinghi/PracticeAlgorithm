#include <iostream>
#include <vector>
#include <cstdio>
#pragma warning(disable : 4996)
using namespace std;
int N, M;
vector<int> V;
bool check[9];
void go()
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
    for (int i = 1; i <= N; i++)
    {
        V.push_back(i);
        go();
        V.pop_back();
    }
}

int main(void)
{
    cin >> N >> M;
    go();
    return 0;
}