#include <stdio.h>
void myprint(int a[10]){
    for(int i=0;i<10;i++) printf("%d ",a[i] );
        printf("\n");
    }


int main()
{

        int a[10]={9,8,7,6,5,4,3,2,1,0};///10數,9個間格
        myprint(a);

        for(int i=0;i<9;i++){///從左到右巡一輪,9個間格
            if(a[i]>a[i+1]){///相鄰比大小,不對
                int temp=a[i];
                a[i]=a[i+1];
                a[i+1]=temp;
            }

            }
