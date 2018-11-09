#Merge Sort
#Time Complexity : O(n(log(n)) and space complexity : O(n)

def merge_sort(in_arr):
    if len(in_arr) > 1:
        middle = len(in_arr)//2 # Taking the floor value of len/2

        left_arr = in_arr[:middle]
        right_arr = in_arr[middle:]

        #Calling merge_sort on the left and the right sub arrays
        merge_sort(left_arr)
        merge_sort(right_arr)

        i,j,k = 0,0,0

        #Merging the results of the two arrays
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                in_arr[k] = left_arr[i]
                i += 1
            else:
                in_arr[k] = right_arr[j]
                j += 1

            k += 1


        #Checking if there are any remaining elements in either of the subarrays
        while i < len(left_arr):
            in_arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            in_arr[k] = right_arr[j]
            j += 1
            k += 1

    return in_arr

#print(merge_sort([1,2,32,1,1,1,1,1,15,6,7,8]))