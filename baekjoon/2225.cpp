#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
    int n, k;
    cin >> n >> k;
    //dp[k][n]
    //n까지의 정수 k개를 더해서 그 합이 n이 되는 경우
	long dp[201][201] = { 0 };
	//init    
	for (int i = 0; i<= n;i++    ) {
		d    [1][i] = 1;
	}
	//n까지의 정 k개 d        k][n]=sigma (dp    k-1    [0~n])
	for (int k1 = 2; k1 <= k; k1++) {
		for (int i    = 0; i <= n; i++) {
			for (int n1         0; n1 <= i; n1++) {
				dp[k1]             += dp[k1-1][n1];
			}
			dp[k1][                 dp[k1][i] % 1000000000;
		            	}            out << dp[k][n] << endl;
	return 0;                    
