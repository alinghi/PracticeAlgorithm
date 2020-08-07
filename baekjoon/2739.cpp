#include <iostream>
using namespace std;


int main(void)
{
    constexpr auto endl = "\n";
    int a;
    cin>>a;

    for (int i=1;i<=9;i++) {
        cout<<a<<" * "<<i<<" = "<<a*i<<endl;
    }

}