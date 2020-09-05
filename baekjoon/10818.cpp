#include <iostream>
using std::cin;
using std::cout;
int main(void)
{
    int a, b;
    int max=-1000000;
    int min=1000000;
    cin>>a;
    for (int i=0;i<a;i++) {
        cin>>b;
        if (b<min) min=b;
        if (b>max) max=b;

    }
    cout<<min<<" "<<max;
}