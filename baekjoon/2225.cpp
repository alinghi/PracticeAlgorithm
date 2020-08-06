#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
	int n, k;
	cin >> n >> k;
	long dp[201][201] ={ 0 };
	//init
	for (int i = 0; i <= n;i++) {
		dp[1][i] = 1;
	}
	for (int k1 = 2; k1 <= k; k1++) {
		for (int i = 0; i <= n; i++) {
			for (int n1 = 0; n1 <= i; n1++) {
				dp[k1][i] += dp[k1-1][n1];
			}
			dp[k1][i] = dp[k1][i] % 1000000000;
		}
	}
	cout << dp[k][n] << endl;
	return 0;
}
