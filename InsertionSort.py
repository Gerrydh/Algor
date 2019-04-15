def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)

start_time = time.time()
print(alist)
end_time = time.time()
time_elapsed = end_time - start_time
print(time_elapsed)

=================================================================================================================================
def insertion_sort(A):
    for i in range(1, len(A)):
       curNum = A[i]
       for j in range(i - 1, 0, -1):
           if A[j] > curNum:
               A[j+1] = A[j]
    else:
                A[j+1] = curNum
                

A = [54,26,93,17,77,31,44,55,20]

print(A)
