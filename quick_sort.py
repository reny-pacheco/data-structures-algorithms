def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater = []
    lower = []

    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)

    return quick_sort(lower) + [pivot] + quick_sort(greater)


print(quick_sort([1,3,5,9,6,-3,78,9,4,-7]))
#prints [-7, -3, 1, 3, 4, 5, 6, 9, 9, 78]