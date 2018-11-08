
#Selection sort algorithm
# Time complexity : O(n^2), Space complexity : O(1)
def selection_sort(in_arr):
    for i in range(0,len(in_arr)-1): #Traversing the array
        min_idx = i #Setting the current index as the index holding the minimum value

        # Iterating the remainder of the array to compare each element and find the
        # minimum element from the remaining elements
        for j in range(i+1, len(in_arr)):
            if in_arr[j] < in_arr[min_idx]:
                min_idx = j
        #Swapping the elements
        in_arr[i], in_arr[min_idx] = in_arr[min_idx], in_arr[i]

    return in_arr


#print(selection_sort([1,2,2,3,4,2,1,2,43,6,8]))