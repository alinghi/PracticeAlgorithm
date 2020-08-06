#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;

int l[250000];

int part(int n, int p) {
	int ret = 0;
	while (n) {
		ret += (int)pow((n % 10), p);
		n = n / 10;
	}
	return ret;
}

int main(void)
{
	int n, p, ans;
	ans = 0;
	cin >> n >> p;
	while (true) {
		l[n]++;
		if (l[n] == 3) {
			break;
		}
		n = part(n, p);
	}
	for (int i = 0; i < 250000; i++) {
		if (l[i] == 1) ans++;
	}
	cout << ans;
}