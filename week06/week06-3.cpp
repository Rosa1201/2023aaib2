/*等差級數列印
輸入首項、公差、項數，輸出前n項
*/
#include <stdio.h>
int main()
{
	int a,b,n;
	scanf("%d %d %d",&a,&b,&n);
	printf("%d",a);
	for(int i=1;i<n;i++){
		a+=b;
		printf(",%d",a);
	}
}
