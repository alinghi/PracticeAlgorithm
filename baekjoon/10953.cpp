#include <iostream>
using namespace std;
#include <cstdio>
int main(void)
{
    int a, b, c;
    char op;
    cin>>c;
    for (int i=0;i<c;i++) {
        cin>>a>>op>>b;
        cout<<a+b<<endl;
    }
}