#---------------------quicksort algorithm implementation----------------
def Quicksort(array,low,high):
#picking a pivot
    pivot = array[low]
    left = low+1
    right = high
    done = False
    while not done:
        while (left<=right and array[left]<=pivot):
            left = left+1
        while (array[right]>=pivot and right>=left):
            right=right-1
        if right<left:
            done = True
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

        temp = array[low]
        array[low] = array[right]
        array[right] = temp
        return right



#-----------------------recurrsion step---------------------------------
def partition(array,low,high):
    if low<high:
        pivot = Quicksort(array,low,high)
        print pivot
        partition(array,low,pivot-1)
        partition(array,pivot+1,high)
    return array

#----------------------------main---------------------------------------
#taking input from user
n = int(input("How many elements you want to enter? "))
inp = []
for i in range(0,n):
    value = int(input("Enter the value at location {} = ".format(i)))
    inp.append(value)

#initializing
start = 0
end = n-1

#printing result
final = partition(inp,start,end)
print final
