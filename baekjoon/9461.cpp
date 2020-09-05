#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
	int num, temp, max;
	max = 0;
	cin >> num;
	vector<int> input;
	for (int i = 0; i < num; i++) {
		cin >> temp;
		if (max < temp) max = temp;
		input.push_back(temp);
	}
	vector<unsigned long long int> dp(101, 0);
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;
	dp[6] = 3;
	dp[7] = 4;
	dp[8] = 5;
	dp[9] = 7;
	dp[10] = 9;
	dp[11] = 12;
	for (int k = 12; k <= max; k++) {
		dp[k] = dp[k - 1] + dp[k - 5];
	}
	for (int i = 0; i < num; i++) {
		cout << dp[input[i]] << endl;
	}
	return 0;
}
