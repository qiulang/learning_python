def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        # Don't forget to return something!
        # Just use the + operator to join lists
        return sort(less)+equal+sort(greater)
    # Note that you want equal ^^^^^ not pivot
    # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
    else:
        return array


def quicksort(xs):
    if xs:
        return (quicksort([i for i in xs[1:] if i < xs[0]])
                + [xs[0]]
                + quicksort([i for i in xs[1:] if i >= xs[0]]))
    else:
        return xs


def partition(a_list, low, high):
    tmp = (low+high)//2
    pivot = a_list[tmp]
    while True:
        while a_list[low] < pivot:
            low += 1
        while a_list[high] > pivot:
            high -= 1
        if low >= high:
            return high
        a_list[low], a_list[high] = a_list[high], a_list[low]
        low += 1
        high -= 1


def quicksort2(a_list):
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""
    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p+1, high)
        # else:
        #     print(f"will this happen ? {low} vs {high}")
    _quicksort(a_list, 0, len(a_list)-1)
    return a_list


array = [12, 4, 5, 6, 7, 3, 1, 5]
# print(sort(array))
quicksort2(array)
print(array)
