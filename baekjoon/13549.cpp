#include <iostream>
#include <deque>
using namespace std;
#define MAX 100001
bool visit[MAX] = {false};
int time[MAX] = {0};
int main()
{
    int N, M;
    cin >> N >> M;
    visit[N] = true;
    time[N] = 0;
    deque<int> q;
    q.push_back(N);
    while (q.size())
    {
        int now = q.front();
        q.pop_front();
        if (now * 2 < MAX)
        {
            if (!visit[now * 2])
            {
                q.push_front(now * 2);
                visit[now * 2] = true;
                time[now * 2] = time[now];
            }
        }
        if (now - 1 >= 0)
        {
            if (!visit[now - 1])
            {
                q.push_back(now - 1);
                visit[now - 1] = true;
                time[now - 1] = time[now] + 1;
            }
        }
        if (now + 1 < MAX)
        {
            if (!visit[now + 1])
            {
                q.push_back(now + 1);
                visit[now + 1] = true;
                time[now + 1] = time[now] + 1;
            }
        }
    }
    cout << time[M] << endl;
    return 0;
}