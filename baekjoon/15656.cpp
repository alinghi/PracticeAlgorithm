#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#pragma warning(disable : 4996)
using namespace std;
int N, M;
vector<int> V;
bool check[9];
void go(vector<int> &input)
{
    if (V.size() == M)
    {
        for (vector<int>::iterator it = V.begin(); it != V.end(); it++)
        {
            printf("%d ", input[*it]);
        }
        puts("");
        return;
    }
    for (int i = 0; i < N; i++)
    {
        V.push_back(i);
        go(input);
        V.pop_back();
    }
}

int main(void)
{
    cin >> N >> M;
    vector<int> input;
    int temp;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input.push_back(temp);
    }
    sort(input.begin(), input.end());
    go(input);
    return 0;
}