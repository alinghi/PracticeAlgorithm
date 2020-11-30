#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#pragma warning(disable : 4996)
#pragma comment(linker, "/STACK:336777216")
using namespace std;
int N, M;
vector<int> v;

void go(vector<int> &in)
{
    if (v.size() == M)
    {
        for (auto it : v)
        {
            printf("%d ", it);
        }
        puts("");
        return;
    }
    for (int i = 0; i < in.size(); i++)
    {
        v.push_back(in[i]);
        go(in);
        v.pop_back();
    }
    return;
}
int main()
{
    cin >> N >> M;
    int temp;
    vector<int> input;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input.push_back(temp);
    }
    sort(input.begin(), input.end());
    input.resize(unique(input.begin(), input.end()) - input.begin());
    go(input);
    return 0;
}