#include <stdio.h>
 
int main(int argc, char** argv) {
    int n, num;
    int readyToWork = 0, untreatedCrimes = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &num);
        if (num > 0) readyToWork += num;
        else {
            if (readyToWork > 0) readyToWork--;
            else untreatedCrimes++;
        }
    }
    printf("%d", untreatedCrimes);
}
