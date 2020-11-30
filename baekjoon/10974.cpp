#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#pragma warning(disable : 4996)
using namespace std;
bool anext_permutation(vector<int> &a)
{
    int i = a.size() - 1;
    while (i > 0 && a[i - 1] >= a[i])
        i--;
    if (i <= 0)
        return false;
    int j = a.size() - 1;
    while (a[j] <= a[i - 1])
        j--;
    int temp = a[j];
    a[j] = a[i - 1];
    a[i - 1] = temp;
    j = a.size() - 1;
    reverse(a.begin() + i, a.end());
    return true;
}

int main(void)
{
    int n;
    cin >> n;
    vector<int> x;
    for (int i = 1; i <= n; i++)
    {
        x.push_back(i);
    }
    do
    {
        for (vector<int>::iterator it = x.begin(); it != x.end(); it++)
        {
            printf("%d ", *it);
        }
        puts("");
    } while (anext_permutation(x));
}