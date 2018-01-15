def mergesort(array):
    l = len(array)
    if l < 2:
        return array
    
    half1 = mergesort(array[:l//2+l%2])
    half2 = mergesort(array[l//2+l%2:])

    i = 0
    j = 0
    s1 = len(half1)
    s2 = len(half2)
    
    result = []
    while i < s1 and j < s2:
        item1 = half1[i]
        item2 = half2[j]
        if item1 <= item2:
            result.append(item1)
            i += 1
        else:
            result.append(item2)
            j += 1

    # broken loop
    if i < s1:
        result += half1[i:]
    else:
        result += half2[j:]

    return result

import random
random.seed()
print(mergesort([((-1)**i)*(random.randint(1,i)) for i in range(21,1,-1)]))

