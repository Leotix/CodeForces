#include <stdio.h>
 
void swap(int x[]) {
	int tmp = x[0];
	x[0] = x[1];
	x[1] = x[2];
	x[2] = tmp;
}
int abs(int num) {
	if (num < 0) num = -num;
	return num;
}
int main(int argc, char** argv) {
	int x[3], num;
	for (int i = 0; i < 3; i++) {
		scanf("%d", &num);
		x[i] = num;
	}
	int p = 0;
	
	while (1) {
		if ((x[0] <= x[1] && x[1] <= x[2]) || (x[2] <= x[1] && x[1] <= x[0])) {
			p = x[1];
			break;
		}
		else swap(x);
	}
	int p1 = abs(p - x[0]);
	int p2 = abs(p - x[2]);
	int distance = p1 + p2;
	printf("%d", distance);
}
