#include <iostream>
using namespace std;
int main(void)
{
	constexpr auto endl = "\n";
	int cal[13] ={ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	string date[7] ={ "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
	int month, day;
	int ans=0;
	cin >> month >> day;
	for (int i = 1; i < month; i++) {
		ans += cal[i];
	}
	ans += day;
	cout << date[ans%7];
}