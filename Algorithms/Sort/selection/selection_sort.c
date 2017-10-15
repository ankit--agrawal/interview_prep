#include"stdio.h"
#include"stdlib.h"
int main()
{
int *array,n=0,i=0,j=0,count=0,min=0,min_loc=0;
printf("\nEnter the number of elements = ");
scanf("\n%d",&n);

array = (int *)malloc(sizeof(int)*n);
	for(i=0;i<n;i++){
		printf("\n Enter element at location %d = ",i);
		scanf("\n%d",&array[i]);
	}
		for(i=0;i<n-1;i++){
			min = array[i];
			min_loc = i;
			for(j=i+1;j<n;j++){
				if(array[j]<min){
					min = array[j];
					min_loc = j;
				}
			}
			array[min_loc] = array[i];
			array[i] = min;
		}
	printf("Sorting array\n");
	for(i=0;i<n;i++){
		printf("The element at location %d = %d\n",i,array[i]);
	}
}
