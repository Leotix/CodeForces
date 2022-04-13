#include <stdio.h>
 
int main(){
	int limak, bob, i = 0;
	scanf("%d %d", &limak, &bob);
	while(1){
		limak = 3*limak;
		bob = 2*bob;
		i++;
		if(limak > bob){
			printf("%d",i);
			break;
		}
	}
}
