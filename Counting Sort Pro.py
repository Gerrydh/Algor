# Ger Hanlon. May 2019. Counting Sort
# Source Code- https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php

import time
start_time = time.time()

# create a count list and using the index to map to the integer in array1.
def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array1:
    # count the number of occurances occurences
    # Store count for each element
        count[a] += 1    
    
    # Sort in place, copy back into original file
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1

print(counting_sort( [list], 15000 ))

End_time = time.time()
Time_lapsed = end_time - start_time
print(time_lapsed)

