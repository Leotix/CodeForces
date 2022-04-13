#include <stdio.h>
int main(){
	int n, least, most, counter = 0, i;
	scanf("%d",&n);
	int a[n];
	for(i = 0; i < n; i++){
		scanf("%d", &a[i]);
	}
	least = a[0];
	most = a[0];
	for(i = 0; i < n; i++){
		if(a[i] > most){
			most = a[i];
			counter++;
		}
		else if(a[i] < least){
			least = a[i];
			counter++;
		}
	}
	printf("%d",counter);
}
