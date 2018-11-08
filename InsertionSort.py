#Insertion sort
# Time complexity : O(n^2), Space complexity : O(1)
def insertion_sort(in_arr):
    arr_len = len(in_arr) #Calculating length of input array

    for i in range(1,arr_len): # iterating through the array starting from 1 to arr_len-1
        curr = in_arr[i] #hold current element in a variable
        j = i - 1

        while j>= 0 and in_arr[j] > curr : # Iterate through the array before the current element
            in_arr[j+1] = in_arr[j] #Shift elements greater than the current element to the right
            j -= 1
        in_arr[j+1] = curr # Place the current element at the right position
    return in_arr


print(insertion_sort([4,3,2,1,1,1,7,8,0,8])) #Testing the function


