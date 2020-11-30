#include <iostream>
#include <deque>
#include <map>
using namespace std;
int N, K;
deque<int> frontier;
bool visited[200000 + 3] = {false};
int BFS()
{
    if (N == K)
        return 0;
    visited[N] = true;
    frontier.push_back(N);
    int time = 1;
    while (frontier.size())
    {
        deque<int> next;
        for (deque<int>::iterator it = frontier.begin(); it != frontier.end(); it++)
        {
            if (*it + 1 == K || *it - 1 == K || *it * 2 == K)
                return time;
            if (*it + 1 <= 100000 && !visited[*it + 1])
            {
                visited[*it + 1] = true;
                next.push_back(*it + 1);
            }
            if (*it - 1 >= 0 && !visited[*it - 1])
            {
                visited[*it - 1] = true;
                next.push_back(*it - 1);
            }
            if (*it * 2 <= 100000 && !visited[*it * 2])
            {
                visited[*it * 2] = true;
                next.push_back(*it * 2);
            }
        }
        frontier = next;
        time++;
    }

    return -1;
}
int main(void)
{
    cin >> N >> K;
    cout << BFS();
    return 0;
}