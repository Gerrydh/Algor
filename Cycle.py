import time
start_time = time.time()

def cycleSort(array): 
  writes = 0
    
  # Loop through the array to find cycles to rotate. 
  for cycleStart in range(0, len(array) - 1): 
    item = array[cycleStart] 
      
    # Find where to put the item. 
    pos = cycleStart 
    for i in range(cycleStart + 1, len(array)): 
      if array[i] < item: 
        pos += 1
      
    # If the item is already there, this is not a cycle. 
    if pos == cycleStart: 
      continue
      
    # Otherwise, put the item there or right after any duplicates. 
    while item == array[pos]: 
      pos += 1
    array[pos], item = item, array[pos] 
    writes += 1
      
    # Rotate the rest of the cycle. 
    while pos != cycleStart: 
        
      # Find where to put the item. 
      pos = cycleStart 
      for i in range(cycleStart + 1, len(array)): 
        if array[i] < item: 
          pos += 1
        
      # Put the item there or right after any duplicates. 
      while item == array[pos]: 
        pos += 1
      array[pos], item = item, array[pos] 
      writes += 1
    
  return writes 
    
# driver code  
arr = [9504,
6922,
11253,
10411,
8120,
13380,
112,
13566,
11493,
12078,
5054,
5422,
13276,
13639,
7366,
3083,
716,
11697,
14095,
2496,
2810,
5155,
391,
2078,
5025,
1101,
10560,
11632,
7250,
2812,
7474,
9080,
13860,
12022,
1754,
373,
4494,
14386,
14259,
3250,
3176,
311,
952,
12293,
2862,
12142,
7110,
8842,
5863,
2224,
8218,
7071,
10911,
5530,
11638,
9905,
8191,
5786,
12072,
4801,
5567,
2155,
6380,
13428,
8711,
1733,
9162,
1718,
8019,
13032,
14312,
5688,
7218,
12462,
2883,
7827,
8668,
8513,
9012,
2320,
3541,
9957,
227,
11146,
2241,
2922,
984,
8958,
10250,
1670,
10249,
9463,
2799,
13886,
10691,
1785,
12540,
11376,
10278,
3324,
8226,
12791,
1565,
4048,
7003,
10322,
1851,
5351,
319,
9953,
14654,
432,
731,
719,
6763,
13098,
10548,
4971,
9900,
150,
10006,
10763,
1045,
14129,
9955,
1369,
10752,
13786,
1751,
7178,
13589,
4913,
4272,
4814,
5713,
85,
10479,
13959,
4785,
12058,
14619,
13941,
8547,
2525,
8083,
11255,
5730,
1714,
1189,
2927] 
n = len(arr)  
cycleSort(arr) 
  
print("After sort : ") 
for i in range(0, n) :  
    print(arr[i], end = ' ')

end_time = time.time()
time_elapsed = end_time - start_time
print(time_elapsed)
