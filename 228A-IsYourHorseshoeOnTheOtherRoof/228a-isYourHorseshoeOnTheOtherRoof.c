#include <stdio.h>
 
int main(){
	int s[4], i, j, d = 0;
	scanf("%d %d %d %d", &s[0], &s[1], &s[2], &s[3]);
	for(i = 0; i < 4; i++){
		for(j = 0; j < 4; j++){
			if(s[i] == s[j])
				break;
		}
		if(i == j)
			d++;
	}
	printf("%d", 4 - d);
}
