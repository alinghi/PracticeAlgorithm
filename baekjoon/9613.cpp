#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    constexpr auto endl = "\n";
    int n, num, temp, a, b;
    unsigned long long ret;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> num;
        vector<int> p;
        vector<int> ans;
        ret = 0;
        for (int j = 0; j < num; j++) {
            cin >> temp;
            p.push_back(temp);
        }
        for (int k = 0; k < p.size(); k++) {
            for (int l = k + 1; l < p.size(); l++) {
                a = p[k];
                b = p[l];
                if (b > a) {
                    temp = b;
                    b = a;
                    a = temp;
                }
                while (b != 0) {
                    temp = a % b;
                    a = b;
                    b = temp;
                }
                ans.push_back(a);
            }
        }
        for (int k = 0; k < ans.size(); k++) {
            ret += ans[k];
        }
        cout << ret << endl;
    }
}