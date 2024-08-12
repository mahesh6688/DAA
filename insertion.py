array = [5,3,7,1,2]

for i in range(1,len(array)):
    index = i
    for j in range(i-1,-1,-1):
        if array[index] > array[j]:
            break
        else:
            array[index],array[j] = array[j],array[index]
            index = j
print(array)
        


