#include"stdio.h"
#include"stdlib.h"

int main()
{
int n,i=0,j=0,k=0,min=0, size=0,location=0;
int *sort_array;
printf("Enter the size of array= ");
scanf("%d",&n);
sort_array = (int *)malloc(sizeof(int)*n);

	for (i=0;i<n;i++){
		printf("Enter element number %d =",i);
		scanf("\n%d",&sort_array[i]);
	}

	while (size != n - 1 ){
		for (i=size;i<n - 1;i++){
			min = sort_array[i];
			location = i;
			for (j=i+1;j<n;j++){
				if (sort_array[j]<min){					
					min = sort_array[j];
					location = j;
				}
			}
			//printf("Minimum for element %d is %d\n", size, min);
			for (k=location-1;k>=size;k--){
				sort_array[k+1] = sort_array[k];
			}
			sort_array[size] = min;
			size = size+1;
		}
	}
	printf("Sorting array...\n");
	for(i=0;i<n;i++){
		printf("Value at location %d is %d\n",i,sort_array[i]);
	}
}
			
