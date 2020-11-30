#include <iostream>
#include <map>
#include <deque>
using namespace std;
int N;
bool visited[2002][2002] = {false};
int BFS()
{
    pair<int, int> s = make_pair(1, 0);
    if (N == 1)
        return 0;
    int i = 1;
    deque<pair<int, int>> frontier;
    frontier.push_back(s);
    visited[1][0] = true;
    while (frontier.size())
    {
        deque<pair<int, int>> next;
        for (deque<pair<int, int>>::iterator it = frontier.begin(); it != frontier.end(); it++)
        {
            int clipboard = (*it).second;
            int current = (*it).first;
            if (current == N || current - 1 == N || current + clipboard == N)
                return i;
            if (clipboard > 0 && current + clipboard < 2002 && !visited[current + clipboard][clipboard])
            {
                visited[current + clipboard][clipboard] = true;
                next.push_back(make_pair(current + clipboard, clipboard));
            }
            if (current - 1 > 0 && current < 2002 && !visited[current - 1][clipboard])
            {
                visited[current - 1][clipboard] = true;
                next.push_back(make_pair(current - 1, clipboard));
            }
            if (current < 2002 && !visited[current][current])
            {
                visited[current][current] = true;
                next.push_back(make_pair(current, current));
            }
        }
        frontier = next;
        i++;
    }
    return 0;
}
int main()
{
    cin >> N;
    cout << BFS();
    return 0;
}