#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#pragma warning(disable : 4996)
using namespace std;
vector<int> x;
vector<int> lotto;

void go(int last_idx)
{
    if (lotto.size() == 6)
    {
        for (auto it : lotto)
            printf("%d ", it);
        puts("");
        return;
    }
    for (int i = last_idx + 1; i < x.size(); i++)
    {
        lotto.push_back(x[i]);
        go(i);
        lotto.pop_back();
    }
    return;
}
int main(void)
{
    int tc;
    tc = 1;
    while (tc)
    {
        cin >> tc;
        if (!tc)
            break;
        int temp;
        x.clear();
        for (int i = 0; i < tc; i++)
        {
            cin >> temp;
            x.push_back(temp);
        }
        go(-1);
        cout << endl;
    }
    return 0;
}