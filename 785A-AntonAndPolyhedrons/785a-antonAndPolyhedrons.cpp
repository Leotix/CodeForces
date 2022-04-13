#include <iostream>
 
using namespace std;
 
int main(){
	int counter = 0, n;
	string s;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> s;
		if(s.compare("Tetrahedron") == 0)
			counter += 4;
		else if(s.compare("Cube") == 0)
			counter += 6;
		else if(s.compare("Octahedron") == 0)
			counter += 8;
		else if(s.compare("Dodecahedron") == 0)
			counter += 12;
		else
			counter += 20;
	}
	printf("%d", counter);
	
}
