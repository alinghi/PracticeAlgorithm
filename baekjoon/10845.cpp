#include <iostream>
#include <string>
#include <queue>
#include <cstdio>
using namespace std;


int main(void)
{
    queue<int> p;
    string x;
    int num, temp;
    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> x;
        if (!x.compare("push")) {
            cin >> temp;
            p.push(temp);
        }
        else if (!x.compare("pop")) {
            if (!p.size()) {
                cout << -1<<endl;
            }
            else {
                cout << p.front() << endl;
                p.pop();
            }
        }
        else if (!x.compare("size")) {
            cout << p.size() << endl;
        }
        else if (!x.compare("empty")) {
            if (!p.size()) {
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
        }
        else if (!x.compare("front")) {
            if (!p.size()) {
                cout << -1 << endl;
            }
            else {
                cout << p.front() << endl;
            }
        }
        else {
            if (!p.size()) {
                cout << -1 << endl;
            }
            else {
                cout << p.back() << endl;
            }
        }
    }
}