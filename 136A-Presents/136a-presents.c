#include <stdio.h>
 
int main(){
	int n, p;
	scanf("%d", &n);
	int tab[n];
	for(int i = 1; i <= n; i++){
		scanf("%d",&p);
		tab[p - 1] = i;
	}
	for(int i = 0; i < n; i++){
		printf("%d ",tab[i]);
	}
		
}
