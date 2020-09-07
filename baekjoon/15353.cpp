#include <iostream>
#include <string>
using namespace std;
int main(void)
{
    string s;
    int result[10002][4] = {0};

    int carry = 0;
    int count = 0;
    getline(cin, s);
    int split = 0;
    for (int i = 0; i < s.length(); i++)
        if (s[i] == ' ')
        {
            split = i;
            break;
        }
    count = 0;
    for (int i = s.length() - 1; i > split; i--)
    {
        result[count++][0] = s[i] - '0';
    }
    count = 0;
    for (int i = split - 1; i >= 0; i--)
    {
        result[count++][1] = s[i] - '0';
    }
    int digit = s.length() - split - 1 > split ? s.length() - split - 1 : split;
    result[0][2] = 0;
    for (int i = 0; i <= digit; i++)
    {
        result[i + 1][2] = (result[i][0] + result[i][1] + result[i][2]) / 10;
        result[i][3] = (result[i][0] + result[i][1] + result[i][2]) % 10;
    }
    for (int i = digit; i >= 0; i--)
    {
        if (i == digit && result[i][3] == 0)
            continue;
        cout << result[i][3];
    }
    return 0;
}