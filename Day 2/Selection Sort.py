list1 = [5,3,8,6,7,2]

for i in range(len(list1)):
    min_index = i
    for j in range(i+1, len(list1)):
        if (list1[j] < list1[i]):
            min_index = j
    list1[i], list1[min_index] = list1[min_index], list1[i]

print(list1)