def quick_sort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[-1]
        left_partition = [x for x in array[:-1] if x <= pivot]
        right_partition = [x for x in array[:-1] if x > pivot]
        return quick_sort(left_partition) + [pivot] + quick_sort(right_partition)

array = [5,7,2,10,9,6,8]
sorted_array = quick_sort(array)
print(sorted_array)
