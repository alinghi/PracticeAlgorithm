#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

void DFS(int start, vector<vector<int>>& graph, vector<int>& visited) {
    visited[start] = true;
    //cout << start << " ";
    for (int i = 0; i < graph[start].size(); i++) {
        if (!visited[graph[start][i]]) {
            DFS(graph[start][i], graph, visited);
        }
    }
    return;
}

void BFS(int start, vector<vector<int>>& graph, vector<int>& visited) {
    visited[start] = true;
    queue<int> bfs;
    bfs.push(start);
    while (bfs.size()) {
        start = bfs.front();
        bfs.pop();
        //cout << start << " ";
        for (int i = 0; i < graph[start].size(); i++) {
            if (!visited[graph[start][i]]) {
                bfs.push(graph[start][i]);
                visited[graph[start][i]] = true;
            }
        }
    }
}


int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    for (int z = 0; z < t; z++) {
        int n;
        cin >> n;
        int a;
        vector<vector<int>> graph(n + 1, vector<int>(0));
        for (int i = 1; i <=n; i++) {
            cin >> a;
            graph[a].push_back(i);
            graph[i].push_back(a);
        }
        for (int i = 0; i < n + 1; i++) {
            sort(graph[i].begin(), graph[i].end());
        }

        vector<int> visited1(n + 1, false);
        visited1[0] = true;
        int ans = 0;
        for (int i = 1; i < n + 1; i++) {
            if (!visited1[i]) {
                DFS(i, graph, visited1);
                ans++;
            }

        }
        cout << ans<<endl;
    }

    return 0;

}