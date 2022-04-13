#include <stdio.h>
 
int main(){
	int n, h, c = 0, a;
	scanf("%d %d", &n, &h);
	for(int i = 0; i < n; i++){
		scanf("%d", &a);
		if(a > h)
			c += 2;
		else{
			c++;
		}
			
	}
	printf("%d",c);
}
