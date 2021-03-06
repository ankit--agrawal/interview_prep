'''The quicksort algorithm implementation when the pivot
		is the middle element'''
def recurrsion_step(input_list,lo,hi):
    #picking a pivot
    i = lo
    j = hi
    done = False
    h = len(input_list)
    if h%2==0:
            pseudo = hi - lo + 1
            index = (pseudo/2) - 1
    else:
            index = (hi-lo)/2
    if index ==0:
	index = lo

    pivot = input_list[index]
    #find correct location of pivot
    while done==False:
	    #checking if the pivot is in the correct location
            while (i<index and input_list[i]<=pivot):
                i=i+1
            while (j>index and input_list[j]>=pivot):
                j=j-1
            #the pivot is in the correct location and the array is sorted
            if i==index and j==index:
                done = True
	    #if not then perform the swaps
            else:
                if input_list[i] > pivot:
                            temp = input_list[i]
                            input_list[i] = input_list[index]
                            input_list[index] = temp
                            index = i
                            done = False
                elif input_list[j] < pivot:
                            temp = input_list[j]
                            input_list[j] = input_list[index]
                            input_list[index] = temp
                            index = j
                            done = False
    '''print "input_list"
    print input_list
    print "------------------------------------" '''
    return index


def partition_input(input_list, low, high):
    if low < high:
	#returning the pivot and recursively running on the left and right partitions
        y = recurrsion_step(input_list,low,high)
        partition_input(input_list,low,y-1)
        partition_input(input_list,y+1,high)
    return input_list

#--------------main-----------------------------------------------
n = raw_input("Enter the number of elements = ")
n = int(n)
input_list = []
for i in range(0,n):
	element = raw_input("Enter the value at location {} = ".format(i))
	element = int(element)
	input_list.append(element)

low = 0
high = n-1
new_list = partition_input(input_list, low, high)
print new_list
