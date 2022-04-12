#include <iostream>
#include <cstring>
using namespace std;
 
int main(){
	string k;
	cin >> k;
	int int_arr[k.length()], lucky = 0;
	
	char arr[k.length()+1];
	strcpy(arr,k.c_str());
	
	for(int i = 0; i < k.length(); i++){
		int_arr[i] = (int)arr[i] - '0';
		if(int_arr[i] == 4 || int_arr[i] == 7)
			lucky++;
	}
	if(lucky == 4 || lucky == 7)
		cout << "YES";
	else
		cout << "NO";
}
