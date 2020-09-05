#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int N, x;
    vector<int> input;
    cin>>N;
    for (int i=0;i<N;i++) {
        cin>>x;
        input.push_back(x);
    }
    if (next_permutation(input.begin(), input.end()))
        for (int i=0;i<N;i++)
            cout<<input[i]<<" ";
    else cout<<-1;
    cout<<endl;

    return 0;
}