#include <stdio.h>
 
int main(){
	long long int s = 0, n;
	scanf("%lld",&n);
	if(n % 2 == 0)
		printf("%lld",n/2);
	else
		printf("%lld",(n-1)/2-n);
}
