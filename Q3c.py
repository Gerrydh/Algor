##Function that returns the duplicates contained in an array
##https://www.geeksforgeeks.org/python-program-print-duplicates-list-integers/

def return_duplicates(elements): ## Define the function return duplicates
    array = len(elements) ## array = all elements of the input range
    duplicates = [] ## duplicates = an empty range currently
    for i in range(array): ## for i the array
        k = i + 1 ## k = the array i and check the next element in the array
        for j in range(k, array): 
            if elements[i] == elements[j] and elements[i] not in duplicates: ## if
                ## the elements of i = the elements of j and elements is not in 
                ## duplicates array 
                 duplicates.append(elements[i]) ## then append the new duplicates 
                                                ## array     
    return duplicates ## when the function has completed its reecursion, return 
                      ## the duplicates
  

test1 = [11, 9, -47, 0, 9, 56, -47, 9, 9]
test2 = [4, 3, 1, 68, 111]
print(return_duplicates(test1)) ## print the dupclicate functions for test1
print(return_duplicates(test2)) ## print the dupclicate functions for test2