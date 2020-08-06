#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
    int num, temp;
    cin >> num;
    vector<int> vec;
    for (int i = 0; i < num; i++) {
        cin >> temp;
        vec.push_back(temp);
    }
    vector<long long> sum(num, 0);
    sum[0] = vec[0];
    for (int i = 1; i < num; i++) {
        if (vec[i] < sum[i - 1] + vec[i]) {
            sum[i] = sum[i - 1] + vec[i];
        }
        else {
            sum[i] = vec[i];
        }
    }
    long long max = -9876543210;
    for (int i = 0; i < num; i++) {
        if (max < sum[i]) max = sum[i];
    }
    cout<<max<<endl;
    return 0;
}