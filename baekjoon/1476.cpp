#include <iostream>
using namespace std;
main(){int E,S,M;cin>>E>>S>>M;int e=1,s=1,m=1,i=1;
while (1){if(e==E &&s==S && m==M) break;e++;s++;m++;i++;if(e>15) e=1;if(s>28) s=1;if(m>19) m=1;}
cout<<i<<endl;return 0;}