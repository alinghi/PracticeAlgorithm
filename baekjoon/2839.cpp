#include <iostream>
using namespace std;

int main(void)
{
    int input;
    int flag=0;
    int iter;
    int largest=0;
    cin>>input;
    iter=input/5;
    for (int a=0;a<=iter;a++)
    {
        if ((input-5*a)%3==0)
        {
            flag=1;
            largest=a;
        }
    }
    if (!flag)
        cout<<-1<<endl;
    else
        cout<<largest+(input-5*largest)/3<<endl;

    return 0;
}