#include"stdio.h"
#include"stdlib.h"

main()
{
	int loop = 0, n , i, j, min, min_loc;
	int *Sort_Array;
	int temp = 0;
	printf("Enter the size of the array");
	scanf("%d", &n);
	Sort_Array = (int *)malloc(sizeof(int)*n);

	printf("Enter the elements of the array\n");
	for(loop = 0; loop < n; loop++)
	{
		printf("Enter element number %d = ",loop);
		scanf("%d", &Sort_Array[loop]);
	}


	for(i = 0; i < n-1; i++)
	{
		min = Sort_Array[i];
		min_loc = i;
		j = i + 1;
		while(j < n)
		{
			if(Sort_Array[j] < min)
			{
				min = Sort_Array[j];
				min_loc = j;
			}
			j++;
		}
		for(j = min_loc; j > i; j--)
		{
			temp = Sort_Array[j];
			Sort_Array[j] = Sort_Array[j-1];
			Sort_Array[j-1] = temp;
		}
	}

	printf("After Insertion\n");
	for(loop = 0; loop < n; loop++)
	{
		printf("Element at value %d is %d\n",loop,Sort_Array[loop]);
	}
}
