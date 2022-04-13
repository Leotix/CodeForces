#include <stdio.h>
 
int main(){
	int x, counter = 0;
	scanf("%d",&x);
	for(int i = 5; i > 0; i--){
	    while(x - i >= 0){
	        counter++;
	        x -= i;
	    }
	}
	printf("%d",counter);
}
