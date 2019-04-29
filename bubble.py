import time
import numpy as np 

numruns = 10
results = []

for r in range (numruns):

    start_time = time.time()

def bubblesort(a):
    for passnum in range(len(a)-1, 0, -1):
        for i in range(passnum):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
a = np.random.randint(0, 10, 100)
bubblesort(a)

end_time = time.time()

time_elapsed = end_time - start_time
results.append(time_elapsed)
print(time_elapsed)
