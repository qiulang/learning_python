def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    # print('merge', result)
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    # print("left", left)
    # print("right", right)
    return merge(left, right)


def binary_search(array, input, start):
    print("search", array, start)
    tmp = len(array)
    if tmp == 1:
        if (array[0] == input):
            return start
        else:
            return -1
    middle = tmp//2
    candidate = array[middle]
    if candidate == input:
        return start+middle
    if candidate > input:
        return binary_search(array[:middle], input, start)
    else:
        return binary_search(array[middle+1:], input, middle+1+start)


def sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))


def partition(sub):
    pivot = sub[-1]
    sub2 = sub[:-1]
    index = len(sub)-1
    for i, val in enumerate(sub2):
        if val > pivot:
            # del sub() 算法不对，先用remove
            sub.remove(val)
            sub = sub+[val]
            index -= 1
    return (index, sub)


def quick_sort(array):
    print("quick sort", array)
    tmp = len(array)
    if tmp <= 1:
        return array
    (pivot, arr) = partition(array)
    print(pivot, arr)
    if (tmp == 2):
        return arr
    if (pivot > 0):
        left = quick_sort(arr[:pivot])
    else:
        left = arr
    if (pivot < len(arr)-2):
        right = quick_sort(arr[pivot+1:])
    else:
        right = arr[pivot+1:]
    a2 = left + [arr[pivot]] + right
    # print(a2)
    return a2
    # quick_sort(array[:pivot])
    # quick_sort(array[pivot+1:])


array = [4, 2, 3, 8, 20, 34, 43, 6, 1, 0]
# array = [4, 2, 1, 9, 3, 8, 5]
# print('merge sort :', array)
ar = merge_sort(array)
print(ar, sorted(ar))
# index = binary_search(ar, 20, 0)
# print(index, ":", ar[index])
ar2 = [8, 34, 6, 0, 2, 8, 34, 6, 1]
a3 = quick_sort(ar2)
print(a3)
