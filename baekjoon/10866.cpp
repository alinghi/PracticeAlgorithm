#include <iostream>
#include <string>
#include <deque>
#include <cstdio>
using namespace std;


int main(void)
{
    deque<int> p;
    string x;
    int num, temp;

    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> x;
        if (!x.compare("push_front")) {
            cin >> temp;
            p.push_front(temp);
        }
        else if (!x.compare("push_back")) {
            cin >> temp;
            p.push_back(temp);
        }
        else if (!x.compare("pop_front")) {
            if (!p.size()) {
                cout << -1 << endl;
            }
            else {
                cout << p.front() << endl;
                p.pop_front();
            }
        }
        else if (!x.compare("pop_back")) {
            if (!p.size()) {
                cout << -1 << endl;
            }
            else {
                cout << p.back() << endl;
                p.pop_back();
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
        else if (!x.compare("back")) {
            if (!p.size()) {
                cout << -1 << endl;
            }
            else {
                cout << p.back() << endl;
            }
        }
    }
}