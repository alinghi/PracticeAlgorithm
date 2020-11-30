#include <iostream>
#include <algorithm>
#include <vector>
#pragma warning(disable : 4996)
using namespace std;
int N, M;
void dfs(int x, int count, bool (&visited)[2000], vector<int> (&edge)[2000])
{
    visited[x] = true;
    if (count == 4)
    {
        cout << 1;
        exit(0);
    }
    for (int i = 0; i < edge[x].size(); i++)
    {
        if (!visited[edge[x][i]])
        {
            dfs(edge[x][i], count + 1, visited, edge);
        }
    }
    visited[x] = false;
}

int main(void)
{

    cin >> N >> M;
    bool visited[2000] = {false};
    vector<int> edge[2000];
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    for (int i = 0; i < N; i++)
    {
        dfs(i, 0, visited, edge);
    }
    cout << 0;
    return 0;
}