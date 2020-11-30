#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;
char alpha[256];
int calc(vector<string> &input, set<char> &letters, vector<int> &candidate)
{
    int sum = 0;
    int i = 0;
    for (set<char>::iterator it = letters.begin(); it != letters.end(); it++)
    {
        alpha[*it] = candidate[i++];
    }
    for (vector<string>::iterator it = input.begin(); it != input.end(); it++)
    {
        int now = 0;
        for (int idx = 0; idx < (*it).size(); idx++)
        {
            now = now * 10 + (alpha[(*it)[idx]]);
        }
        sum += now;
    }
    return sum;
}
int main(void)
{
    int N;
    cin >> N;
    vector<string> input;
    set<char> s;
    string temp;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input.push_back(temp);
        for (int j = 0; j < temp.size(); j++)
        {
            s.insert(temp[j]);
        }
    }
    vector<int> candidate;
    for (int i = 9 - s.size() + 1; i <= 9; i++)
    {
        candidate.push_back(i);
    }
    int ans = 0;
    do
    {
        ans = max(ans, calc(input, s, candidate));
    } while (next_permutation(candidate.begin(), candidate.end()));
    cout << ans << '\n';
    return 0;
}