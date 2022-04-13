#include <stdio.h>
 
int main(){
	int a, b, sum;
	scanf("%d %d", &a, &b);
	if (a > b){
		sum = (a - b)/2;
		printf("%d %d", b, sum);
	}
	else{
		sum = (b - a)/2;
		printf("%d %d", a, sum);
	}
}
