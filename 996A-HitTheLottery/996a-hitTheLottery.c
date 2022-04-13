#include <stdio.h>
 
int main(){
	int n, divided, billsCount = 0, bills[] = {100, 20, 10, 5, 1};
	scanf("%d",&n);
	for(int i = 0; i < 5; i++){
		divided = n/bills[i];
		billsCount += divided;
		n -= divided*bills[i];
	}
	printf("%d",billsCount);
}
