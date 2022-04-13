#include <iostream>
 
using namespace std;
 
int main(){
	int x, c = 0, p, q;
	cin >> x;
	for(int i = 0; i < x; i++){
		cin >> p >> q;
		if(q - p >= 2)
			c++;
	}
	cout << c;
}
