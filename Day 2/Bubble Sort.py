from tempfile import tempdir


list1 = [5,3,8,6,7,2]

count = 1

while (count < len(list1)):
    for i in range(5):
        if (list1[i] > list1[i+1]):
            list1[i], list1[i+1] = list1[i+1], list1[i]
    count+=1

print(list1)