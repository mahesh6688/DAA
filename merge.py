def merge_sort(array):
    if len(array)<=1:
        return array
    else:
        mid = len(array)//2
        left_half = merge_sort(array[:mid])
        right_half = merge_sort(array[mid:])
        return merge(left_half,right_half)

def merge(left,right):
    result = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



array = [5,7,2,10,9,6,8]
sorted_array = merge_sort(array)
print(sorted_array)