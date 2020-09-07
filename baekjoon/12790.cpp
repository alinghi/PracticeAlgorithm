#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    vector<vector<int>> vec(T, vector<int>(8));
    for (int i = 0; i < T; i++)
    {
        for (int j = 0; j < 8; j++)
            cin >> vec[i][j];
    }
    for (int i = 0; i < T; i++)
    {
        int hp = vec[i][0] + vec[i][4];
        if (hp < 1)
            hp = 1;
        int mp = vec[i][1] + vec[i][5];
        if (mp < 1)
            mp = 1;
        int ad = vec[i][2] + vec[i][6];
        if (ad < 0)
            ad = 0;
        int ar = vec[i][3] + vec[i][7];
        cout << hp + 5 * mp + 2 * ad + 2 * ar << endl;
    }
    return 0;
}