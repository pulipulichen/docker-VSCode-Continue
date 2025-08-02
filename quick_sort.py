def quick_sort(arr):
    # 建立快速排序的功能
    if len(arr) <= 1:
        return
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        quick_sort(left)
        quick_sort(right)
        arr[:] = left + middle
        return arr
