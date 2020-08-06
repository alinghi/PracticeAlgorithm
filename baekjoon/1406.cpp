#include <iostream>
#include <list>
#include<string>
using namespace std;

int main(void)
{
    string x;
    int num;
    char cmd;
    cin >> x;
    cin >> num;
    list<char> p(x.begin(), x.end());
    list<char>::iterator cursor = p.end();
    for (int i = 0; i < num; i++) {
        cin >> x;
        if (x[0]=='L') {
            if (cursor != p.begin()) {
                cursor--;
            }
        }
        else if (x[0] == 'D') {
            if (cursor != p.end()) {
                cursor++;
            }
        }
        else if (x[0] == 'B') {
            if (cursor != p.begin()) {
                cursor--;
                cursor=p.erase(cursor);
            }
        }
        else if (x[0] == 'P') {
            cin >> x;
            p.insert(cursor, x[0]);
        }
    }
    for (auto& x : p) {
        cout << x;
    }


    return 0;
}