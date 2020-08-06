#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;
#define RED 0
#define BLACK 1

void DFS(vector<vector<int> >& graph, vector<int>& visited, int start, int color) {
    visited[start] = color;
    for (int i = 0; i < graph[start].size(); i++) {
        if (visited[graph[start][i]]==-1) {
            DFS(graph, visited, graph[start][i], 1 - color);
        }
    }
    return;
}


int main(void)
{
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        int m, n;
        int a, b;

        cin >> m >> n;
        vector<vector<int> > graph(m+1, vector<int>(0));
        vector<int> visited(m + 1, -1);
        for (int j = 0; j < n; j++) {
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        for (int k = 1; k < m + 1; k++) {
            if (visited[k]==-1) {
                DFS(graph, visited, k, RED);
            }
        }
        bool ans = true;
        for (int k1 = 1; k1 < m + 1; k1++) {
            for (int k2 = 0; k2 < graph[k1].size(); k2++) {
                if (visited[k1] == RED) {
                    if (visited[graph[k1][k2]] == RED) {
                        ans = false;
                        break;
                    }
                }
                else if (visited[k1]==BLACK) {
                    if (visited[graph[k1][k2]] == BLACK) {
                        ans = false;
                        break;
                    }
                }
            }
            if (!ans) break;
        }

        if (ans) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}