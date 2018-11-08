#Bubble sort
#Time complexity : O(n^2), Space complexity : O(1)
def bubble_sort(in_arr) :
    for i in range(0, len(in_arr)): # Iterate through the entire array
        for j in range(0, len(in_arr) - i - 1): #Evertime the array elements are placed correctly from the end
            if in_arr[j] > in_arr[j+1]:
                #Swap whenever the next element is greater than the previous
                in_arr[j], in_arr[j+1] = in_arr[j+1], in_arr[j]

    return in_arr


print(bubble_sort([1,2,3,41,2,3,4,5,6,7,432,1,1,1,0,2,-20]))