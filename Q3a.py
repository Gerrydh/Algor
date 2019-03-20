def contains_duplicates(elements):
    
    for i in range(0, len(elements)):
        for j in range (0, len(elements)):
            if i == j:
                continue
            if elements[i] == elements[j]:
                return True
    return False

test1 = [10, 0, 5, 3, -19, 5]
test2 = [0, 1, 0, -127, 346, 125]

print(contains_duplicates(test1))