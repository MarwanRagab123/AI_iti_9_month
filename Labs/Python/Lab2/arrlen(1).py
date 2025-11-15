def arr(length,start):
    array = []
    for i in range(length):
        array.append(start + i)
    return array
print(arr(5, 10))