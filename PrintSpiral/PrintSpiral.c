#include"stdio.h"
main()
{
int m=0,n=0,i=0,j=0,size=0,a=0,b=0,c=0;
//-----------creating the input matrix---------------------------------------------------------------------
printf("enter the number of rows and columns \n");
scanf("%d \n %d",&m,&n);

int input_matrix[m][n];

printf("enter the values of matrix\n");
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			printf("enter the value for location matrix[%d][%d]\n",i,j);
			scanf("%d",&input_matrix[i][j]);
		}
	}
//-----------------test input and formatting------------------------------------------------------------
/*	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			printf("%d\n",input_matrix[i][j]);
		}
	}*/
//-----------------implementation of the cyclic print--------------------------------------------------

b=m-1;
c=n-1;
size = m*n;

	while(size!=0){
		for(i=a;i<=c;i++){
			printf("%d\n",input_matrix[a][i]);
			size = size-1;
		}
		for(j=a+1;j<=b;j++){
			printf("%d\n",input_matrix[j][b]);
			size = size -1;
		}
		for(i=b-1;i>=a;i--){
			printf("%d\n",input_matrix[b][i]);
			size = size -1;
		}
		for(j=b-1;j>a;j--){
			printf("%d\n",input_matrix[j][a]);
			size = size -1;
		}
		a = a+1;
		b = b-1;
		c = c-1;
	}
}
