#include <stdio.h>
 
int main(){
	int x, c = 0, p, q;
	scanf("%d",&x);
	for(int i = 0; i < x; i++){
		scanf("%d %d", &p, &q);
		if(q - p >= 2)
			c++;
	}
	printf("%d",c);
}
