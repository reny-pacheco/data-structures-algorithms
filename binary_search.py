def bs(arr, t):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        mid_value = arr[mid]

        if mid_value == t:
            return mid
        elif t < mid:
            end = mid - 1
        else:
            start = mid + 1
    
    return mid
    
array = [1,2,3,4,5,6,7]
target = 2

print(bs(array,target))
#prints 1