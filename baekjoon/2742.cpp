#include <iostream>
using namespace std;
int main(void) {
    constexpr auto endl = "\n";
    int a;
    cin>>a;
    for (int i=a;i>0;i--) {
        cout<<i<<endl;
    }
}