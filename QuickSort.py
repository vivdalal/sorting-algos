def quick_sort(arr, low, high):
    if low < high:

        part = partition(arr, low, high)

        quick_sort(arr, low, part-1)
        quick_sort(arr, part+1, high)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]   #Taking last element as pivot

    for j in range(low, high):

        if arr[j] <= pivot:
            #Placing all elements smaller than pivot before the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1] #Placing pivot at the right position
    return i+1


in_arr = [10, 5, 50, 40, 60, 80, 20, 20, -20]
quick_sort(in_arr, 0, len(in_arr)-1) #Performing quick sort in a recursive fashion
print("Sorted array: ")
print(*in_arr, sep=", ")




