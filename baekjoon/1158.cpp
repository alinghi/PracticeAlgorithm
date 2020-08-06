#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    int n, k, count1, count2, index;
    cin >> n >> k;

    index = 0;
    count2 = 0;
    vector<bool> p(n, false);
    vector<int> x;
    while (n > count2) {
        count1 = 0;
        while (count1 != k) {
            index = (index + 1) % n;
            if (!p[index]) {
                count1++;
            }
        }
        if (index == 0) {
            x.push_back(n);
        }
        else {
            x.push_back(index);
        }
        p[index] = true;
        count2++;
    }
    cout << "<";
    for (int i = 0; i < x.size() - 1; i++) cout << x[i] << ", ";
    cout << x[x.size() - 1];
    cout << ">";
}