#include <iostream>
using namespace std;

int main(void) {
    int a, b, c;
    cin>>c;
    for (int i=1;i<=c;i++) {
        cin>>a>>b;
        cout<<"Case #"<<i<<": "<<a<<" + "<<b<<" = "<<a+b<<endl;
    }
}