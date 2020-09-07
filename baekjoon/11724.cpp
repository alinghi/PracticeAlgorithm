#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

void DFS(int start, vector<vector<int>> &graph, vector<int> &visited)
{
    visited[start] = true;
    //cout << start << " ";
    for (int i = 0; i < graph[start].size(); i++)
    {
        if (!visited[graph[start][i]])
        {
            DFS(graph[start][i], graph, visited);
        }
    }
    return;
}

void BFS(int start, vector<vector<int>> &graph, vector<int> &visited)
{
    visited[start] = true;
    queue<int> bfs;
    bfs.push(start);
    while (bfs.size())
    {
        start = bfs.front();
        bfs.pop();
        //cout << start << " ";
        for (int i = 0; i < graph[start].size(); i++)
        {
            if (!visited[graph[start][i]])
            {
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

    int n, m, v;
    cin >> n >> m;
    int a, b;
    vector<vector<int>> graph(n + 1, vector<int>(0));
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for (int i = 0; i < n + 1; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }
    /*
	vector<int> visited1(n + 1, false);
	visited1[0] = true;
	int ans = 0;
	for (int i = 1; i < n + 1; i++){
		if (!visited1[i]) {
			DFS(i, graph, visited1);
			ans++;
		}
			
	}
	*/

    int ans = 0;
    vector<int> visited2(n + 1, false);
    visited2[0] = true;
    for (int i = 1; i < n + 1; i++)
    {
        if (!visited2[i])
        {
            BFS(i, graph, visited2);
            ans++;
        }
    }

    cout << ans;
}