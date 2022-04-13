#include <iostream>
 
using namespace std;
 
int main()
{
    int n,i;
    double sum=0.0;
    scanf("%d",&n);
    int a;
    for(i=0;i<n;i++){
        scanf("%d",&a);
        sum+=a;
    }
    sum=sum/n;
    printf("%.12lf\n",sum);
    return 0;
}
