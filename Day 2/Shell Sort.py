list1 = [5,3,8,6,7,2,9,11,23]

size = len(list1)

gap = size//2

while gap > 0:
    for i in range(gap,size):
        anchor = list1[i]
        j = i
        while j>=gap and list1[j-gap] > anchor:
            list1[j] = list1[j-gap]
            j-=gap
        list1[j] = anchor
    gap = gap//2

print(list1)