#include <stdio.h>
int main(){
	int n, k;
	scanf("%d  %d",&n,&k);
	int org_n = n, time_left = 240 - k;
	int i = 1;
	while(time_left >= 0 && n > 0){
		time_left -= 5*i;
		if(time_left < 0)
			break;
		n--;
		i++;
	}
	printf("%d",org_n-n);
}
