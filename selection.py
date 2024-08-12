array = [7,4,5,2,8]

for i in range(0,len(array)-1):
    minvalue_index = i
    for j in range(i+1,len(array)):
        if array[minvalue_index] > array[j]:
            minvalue_index = j
    array[i],array[minvalue_index] = array[minvalue_index],array[i]

print(array)
