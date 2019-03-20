def finder(data): ## define the finder argument (data)
    return finder_rec(data, len(data)-1) ## return the answer

def finder_rec(data, x): ## define the finder_recursive argument as data and x
    if x == 0: ## compares if x is equal to 0, then true
        return data[x] ## return the answer
    v1 = data[x] ## v1 equals the highest value in the range
    v2 = finder_rec(data, x-1) ## v2 equals the lowest value in the range
    if v1 > v2: ## if v1 is greater then v2
        return v1 ## then return v1
    else:
        return v2 ## if not, return v2

print(finder([0, -247, 341, 1001, 741, 22])) ## print the answer from the data ranged passed in