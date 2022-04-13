#include <iostream>
 
using namespace std;
 
int main(){
	string s, n = "";
	int i, j, d = 0;
	getline(cin, s);
	if(!s.compare("{}")){
		printf("%d",0);
		return 0;
	}
	for(i = 1; i < s.length()-1; i++){
		if(i % 3 == 1)
			n += s[i];
	}
	int nLength = n.length();
	for(i = 0; i < nLength; i++){
		for(j = 0; j < nLength; j++){
			if(n[i] == n[j])
				break;
		}
		if(i == j)
			d++;
	}
	printf("%d", d);
}
