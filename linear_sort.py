"""Program will move all zeros to the end of the array."""

def sort_zeros(list1):
    counter = 0
    counterpos = 0
    length = len(list1)
    while counterpos < length:
        counterpos = counterpos + 1
        if list1[counter] == 0:
            value = list1.pop(counter)
            list1.append(value)

        else:
            counter = counter + 1
    return list1


print(sort_zeros([0,9,3,0,1,0,0,0,0,2,6,3,0,0,0,1,3,1,1,1,1,1,0,0,3,2,0,0]))
