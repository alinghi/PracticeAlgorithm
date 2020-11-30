#include <iostream>
#include <vector>
#include <algorithm>
#pragma warning(disable : 4996)
using namespace std;
vector<char> input;
int N, M;
bool check(string s)
{
    int v = 0;
    int c = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            v++;
        }
        else
        {
            c++;
        }
    }
    if (v > 0 && c > 1)
        return true;
    else
        return false;
}
void go(string s)
{
    if (s.size() == N and check(s))
    {
        cout << s << endl;
        return;
    }
    for (int i = s.size() ? find(input.begin(), input.end(), s.at(s.size() - 1)) - input.begin() + 1 : 0; i < input.size(); i++)
    {
        go(s + input[i]);
    }
}
int main(void)
{
    string s = "";
    cin >> N >> M;
    char c;
    for (int i = 0; i < M; i++)
    {
        cin >> c;
        input.push_back(c);
    }
    sort(input.begin(), input.end());
    go("");
    return 0;
}