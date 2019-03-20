def finder(data): ## define the function name
    return finder_rec(data, len(data)-1) ## return the answer

def finder_rec(data, x):
    if x == 0:
        return data [x]
    v1 = data[x] ## v1 = positve x in the data range
    v2 = finder_rec(data, x-1) ## v2 = smallest x in the data range
    if v1 > v2: ## if v1 is greater than v2
        return v1 ## then return the highest value in the range
    else:
        return v2 ## or else return the highest negative value in v2
print(finder([0, -247, 341, 1001, 741, 22, -4, -1001])) ## Call the function