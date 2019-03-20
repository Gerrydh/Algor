def finder(data, x):
    if x == 0:
        return data[x]
    v1 = data[x]
    v2 = finder(data, x-1)
    if v1 > v2:
        return v1
    else:
        return v2

print(finder([0, -247, 341, 1001, 741, 22]))