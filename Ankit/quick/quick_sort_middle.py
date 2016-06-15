'''The quicksort algorithm implementation when the pivot 
		is the middle element'''
def recurrsion_step(input_list,lo,hi):
    #picking a pivot
    h = len(input_list)
    check1 = 0
    check2 = 0
    i = lo
    j = hi
    done = False
    if h%2==0:
            pseudo = hi - lo + 1
            index = (pseudo/2) - 1
    else:
            index = (hi-lo)/2
    if index ==0:
	index = lo

    pivot = input_list[index]
    print "pivot = {}".format(pivot)
    #find correct location of pivot
    while done==False:
            while (i<index and input_list[i]<=pivot):
                i=i+1
            while (j>index and input_list[j]>=pivot):
                j=j-1
                
            if i==index and j==index:
                done = True
            else:
                if input_list[i] > pivot:
                            temp = input_list[i]
                            input_list[i] = input_list[index]
                            input_list[index] = temp
                            index = i
			    print "index after 1st loop = {}".format(index)
                            done = False
                elif input_list[j] < pivot:
                            temp = input_list[j]
                            input_list[j] = input_list[index]
                            input_list[index] = temp
                            index = j
			    print "index after 2nd loop (the value of y) = {}".format(index)
                            done = False
    print "input_list"
    print input_list
    print "------------------------------------"
    return index


def partition_input(input_list, low, high):
    if low < high:
        y = recurrsion_step(input_list,low,high)
        partition_input(input_list,low,y-1)
        partition_input(input_list,y+1,high)
    return input_list

#--------------main-----------------------------------------------
n = raw_input("Enter the number of elements = ")
n = int(n)
input_list = []
for i in range(0,n):
	element = raw_input("Enter the values = ")
	element = int(element)
	input_list.append(element)

low = 0
high = n-1
new_list = partition_input(input_list, low, high)
print new_list
