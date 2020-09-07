#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
    int num, temp;
    vector<unsigned long long int> vec;
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        cin >> temp;
        vec.push_back(temp);
    }
    vector<vector<int>> graph(num, vector<int>(num, 0));
    for (int i = 0; i < num; i++)
    {
        for (int j = i + 1; j < num; j++)
        {
            if (vec[j] < vec[i])
            {
                graph[i][j] = 1;
                //to be unsymmetric matrix
            }
        }
    }
    vector<int> l(num, 1);
    vector<unsigned long long int> sum(num, 0);

    int max = -1;
    for (int i = 1; i < num; i++)
    {
        max = -1;
        int max_position = -1;
        for (int j = 0; j < i; j++)
        {
            if (l[j] > max && graph[j][i])
            {
                max = l[j];
                max_position = j;
            }
        }
        if (max != -1)
        {
            l[i] = max + 1;
        }
    }
    max = -1;
    for (int i = 0; i < num; i++)
    {
        if (max < l[i])
            max = l[i];
    }
    cout << max << endl;
    return 0;
}