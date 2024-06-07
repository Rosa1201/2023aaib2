#include <stdio.h>
void myprint(int a[10]){
    for(int i=0;i<10;i++) printf("%d ",a[i] );
        printf("\n");
    }


int main()
{

        int a[10]={9,8,7,6,5,4,3,2,1,0};///10數,9個間格
        myprint(a);

    for(int i=0;i<10;i++){///for迴圈k重複很多次
        for(int j=0;j<10;j++){///從左到右巡一輪,9個間格
            if(a[i]>a[j]){///相鄰比大小,不對
                int temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }

            }
        myprint(a);
    }
}
