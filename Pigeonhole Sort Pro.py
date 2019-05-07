 # Pigeonhole Sorting Algorithm. Ger Hanlon. April 2019  
 # source code : "https://en.wikibooks.org/wiki/ 


# Import the time module
import time

start_time = time.time()

def pigeonhole_sort(a): 
    # size of range of values in the list  
    # (ie, number of pigeonholes we need) 
    my_min = min(a) 
    my_max = max(a) 
    size = my_max - my_min + 1
  
    # our list of pigeonholes 
    holes = [0] * size 
  
    # Populate the pigeonholes. 
    for x in a: 
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
  
    # Put the elements back into the array in order. 
    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            a[i] = count + my_min 
            i += 1
              
# Pass in the randonmly generated values to be sorted 
a = [] 
print("Sorted order is : ", end = ' ') 
  
pigeonhole_sort(a) 
          
for i in range(0, len(a)): 
    print(a[i], end = ' ') 

# generate the elapsed time by taking away the start time from the end time
end_time = time.time()
time_elapsed = end_time - start_time
print(time_elapsed)
