#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;


int main(void)
{
    string x;
    int small, big, number, blank;
    vector<int> p(26, -1);
    while (getline(cin, x)) {
        small = 0;
        big = 0;
        number = 0;
        blank = 0;
        for (int i = 0; i < x.size(); i++) {
            if (x[i] >= 'A' && x[i] <= 'Z') big++;
            if (x[i] >= 'a' && x[i] <= 'z') small++;
            if (x[i] >= '0' && x[i] <= '9') number++;
            if (x[i] == ' ') blank++;
        }
        cout << small << " " << big << " " << number << " " << blank << endl;
    }
}