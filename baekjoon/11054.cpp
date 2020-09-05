#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
    int num, temp;
    vector<unsigned long long int> vec;
    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> temp;
        vec.push_back(temp);
    }
    vector<vector<int>> graph1(num, vector<int>(num, 0));
    vector<vector<int>> graph2(num, vector<int>(num, 0));
    for (int i = 0; i < num; i++) {
        for (int j = i + 1; j < num; j++) {
            if (vec[j] > vec[i]) {
                graph1[i][j] = 1;
                //to be unsymmetric matrix
            }
            if (vec[num-j-1] > vec[num-i-1]) {
                graph2[i][j] = 1;
                //to be unsymmetric matrix
            }
        }
    }
    vector<int> l1(num, 1);
    vector<int> l2(num, 1);
    vector<int> sum(num, 0);

    int max1 = -1;
    int max2 = -1;
    for (int i = 1; i < num; i++) {
        max1 = -1;
        max2 = -1;
        int max_position = -1;
        for (int j = 0; j < i; j++) {
            if (l1[j] > max1 && graph1[j][i]) {
                max1 = l1[j];
            }
            if (l2[j] > max2 && graph2[j][i]) {
                max2 = l2[j];
            }
        }
        if (max1 != -1) {
            l1[i] = max1 + 1;
        }
        if (max2 != -1) {
            l2[i] = max2 + 1;
        }
    }
    for (int i = 0; i < num; i++) {
        sum[i] = l1[i] + l2[num - i - 1];
    }
    int max = 0;
    for (int i = 0; i < num; i++) {
        if (max < sum[i]) max = sum[i];
    }

    cout << max-1 << endl;
    return 0;
}