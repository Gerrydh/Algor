def contains_duplicates(elements): ## Define the function contains_duplicates
    for i in range(0, len(elements)): ## for all of the elements in the range
        for j in range(0, len(elements)): ## all of the emelemts in the range
            if i == j: ## do not compare to self
                continue ## continue
            if elements[i] == elements[j]: ## if any of the elements are the same
                return True ## return True
    return False ## if none of the elments are duplicates then return False

test1 = [10, 0, 5, 3, -19, 5]
test2 = [1, 0, -127, 346, 125]

print(contains_duplicates(test2))