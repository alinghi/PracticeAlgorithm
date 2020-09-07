#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    int a, b;
    cin >> a >> b;
    int num, temp;
    cin >> num;
    vector<int> p;
    vector<int> p1;
    for (int i = 0; i < num; i++)
    {
        cin >> temp;
        p.push_back(temp);
    }
    temp = 1;
    unsigned int ans = 0;
    for (int i = 0; i < num; i++)
    {
        ans += p[p.size() - 1 - i] * temp;
        temp = temp * a;
    }
    while (ans != 0)
    {
        p1.push_back(ans % b);
        ans = ans / b;
    }
    for (int i = 0; i < p1.size(); i++)
    {
        cout << p1[p1.size() - i - 1] << " ";
    }
}