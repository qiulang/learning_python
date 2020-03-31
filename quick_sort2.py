# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition_r(arr, lo, hi):
    pivot = (lo+hi)//2
    print(f"pivot:{arr[pivot]}, partition from {lo} to {hi} of {arr}")
    arr[pivot], arr[hi] = arr[hi], arr[pivot]
    return partition(arr, lo, hi)


def partition(arr, low, high):
    i = low         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low, high, 1):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i+1

    arr[i], arr[high] = arr[high], arr[i]
    return i

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition_r(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# ar = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
ar = [12, 4, 5, 6, 7, 3, 1, 15]
# ar = [4, 6, 3]
quickSort(ar, 0, len(ar)-1)
print(ar)


def quicksort2(a, lo, hi):
    while(lo < hi):
        pivot = a[lo]
        i = lo+1
        for j in range(lo+1, hi+1):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        i -= 1
        a[i], a[lo] = a[lo], a[i]
        if(i - lo <= hi - i):
            quicksort2(a, lo, i-1)
            lo = i+1
        else:
            quicksort2(a, i+1, hi)
            hi = i-1


# ar = [4, 6, 3]
# ar = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
# quicksort2(ar, 0, len(ar)-1)
# print(ar)
