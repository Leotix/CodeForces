#include <iostream>
#include <cstring>
 
using namespace std;
int main() {
	bool same = true;
	string n, t;
	cin >> n;
	cin >> t;
	int size = n.length();
	for (int i = 0, j = size-1; i < size && j >= 0; i++, j--) {
		if (n[i] != t[j])
			same = false;
	}
	if (same == true)
		cout << "YES";
	else
		cout << "NO";
 
}
