#include <stdio.h>
  
void swap(int *xp, int *yp) 
{ 
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
} 
  
void bubbleSort(int arr[], int n) 
{ 
   int i, j; 
   for (i = 0; i < n-1; i++)         
       for (j = 0; j < n-i-1; j++)  
           if (arr[j] > arr[j+1]) 
              swap(&arr[j], &arr[j+1]); 
} 
 
int main(){
	int x1, x3, x4, tab[4];
	for(int i = 0; i < 4; i++){
		scanf("%d", &tab[i]);
	}
	bubbleSort(tab, 4);
	x1 = tab[0];
	x3 = tab[2];
	x4 = tab[3];
	printf("%d %d %d",x4 - x3,x1 - x4 + x3,x4 - x1);
	
	
}
