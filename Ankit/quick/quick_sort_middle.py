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
            index = pseudo/2
    else:
            index = (hi-lo)/2

    pivot = input_list[index]
    
    #find correct location of pivot
    #for k in range(0,h):
    while not done:
            check1 = 0
            check2 = 0
            '''for i in range(0,index):
                    if input_list[i] > input_list[index]:
                            temp = input_list[i]
                            input_list[i] = input_list[index]
                            input_list[index] = temp
                            index = i
                            check1 = 0
                            break
                    else:
                        check1 = 1'''
            while (i<=index and input_list[i]<=pivot):
                i=i+1
                check1 = 1
            while (j>=index and input_list[j]>=pivot):
                j=j-1
                check2 = 1
                
            '''for i in range(h-1,index,-1):
                    if input_list[i] < input_list[index]:
                            temp = input_list[i]
                            input_list[i] = input_list[index]
                            input_list[index] = temp
                            index = i
                            check2 = 0
                            break
                    else:
                        check2 = 1'''
            if check1==1 and check2==1:
                done = True
            else:
                if input_list[i] > input_list[index]:
                            temp = input_list[i]
                            input_list[i] = input_list[index]
                            input_list[index] = temp
                            index = i
                            done = False
                elif input_list[j] < input_list[index]:
                            temp = input_list[j]
                            input_list[j] = input_list[index]
                            input_list[index] = temp
                            index = j
                            done = False
    print input_list
    print index
    return index


def partition_input(input_list, low, high):
    if low < high:
        y = recurrsion_step(input_list,high,low)
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
