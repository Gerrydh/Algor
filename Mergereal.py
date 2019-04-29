import time

start_time = time.time()

def mergeSort(alist):

   print("Splitting ",alist)

   ## if the list is less than or equal to one, no more sorting required. If list is greater than 1 then slice  the left 
   ## and right  halves of the list  
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",alist)
num_runs = 20
results = []
for r in range (num_runs):

    alist = []
mergeSort(alist)
print(alist)
end_time = time.time()
time_elapsed = end_time - start_time
print(time_elapsed)
results.append(time_elapsed)
