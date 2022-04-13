#include <stdio.h>
 
int main(){
	int t, a, b, i;
	scanf("%d",&t);
	int tab[t];
	for(i = 0; i < t; i++){
		scanf("%d %d", &a, &b);
		if(a % b == 0)
			tab[i] = 0;
		else
			tab[i] = b - a % b;
	}
	for(i = 0; i < t; i++)
		printf("%d\n", tab[i]);
}
