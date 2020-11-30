#include <iostream>
using namespace std;
void calc(int a, int b, int c, int d) {
	c = c - 1;
	d = d - 1;
	int y = c ;
	int x = (c ) % b;
	int count = 0;
	while (x != d) {
		x = (x + (a - b)+b) % b;
		y = y + a;
		count++;
		if (count > b + 2) {
			cout << -1 << endl;
			return;
		}
	}
	cout << y+1 << endl;
}
int main(void) {
	int tc,a, b, c, d;
	cin >> tc;
	for (int i = 0; i < tc; i++) {
		cin >> a >> b >> c >> d;
		calc(a, b, c, d);
	}
	return 0;
}