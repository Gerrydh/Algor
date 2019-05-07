# Ger Hanlon. April 2019. Insertion Sort
# Source Code- https://www.geeksforgeeks.org/python-program-for-insertion-sort/


import time 

start_time = time.time()


def insertionSort(alist):
   for index in range(1,len(alist)):

    # the element to be compared
     currentvalue = alist[index]
     position = index

    # compare the current element with the sorted position and swaping
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = []
insertionSort(alist)

print(alist)
end_time = time.time()
time_elapsed = end_time - start_time
print(time_elapsed)
