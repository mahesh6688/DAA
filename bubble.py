array = [5,2,9,1,0,7,6]
for i in range(0,len(array)):
    for j in range(0,len(array)-1):
        if array[j]>array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
print(array)