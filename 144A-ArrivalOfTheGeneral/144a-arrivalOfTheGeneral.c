#include <stdio.h>
 
int main(){
	int n, i, j, min = 101, max = 0, maxInd, minInd;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf("%d", &j);
		if(j > max){
			max = j;
			maxInd = i;
		}
		if(j <= min){
			min = j;
			minInd = i;
		}
	}
	if(maxInd > minInd){
		printf("%d", (maxInd - 1) + (n - minInd) - 1);
	}
	else{
		printf("%d", (maxInd - 1) + (n - minInd));
	}
 
}
