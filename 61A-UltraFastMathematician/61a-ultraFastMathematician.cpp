#include <iostream>
using namespace std;
 
int main(){
	string s1, s2;
	cin >> s1 >> s2;
	for(int i = 0; i < s1.length(); i++){
		printf("%d", (s1[i] - '0') ^ (s2[i] - '0'));
	}
}
