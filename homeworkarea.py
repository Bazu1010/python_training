## Test how long your program takes to loop through 10,000 values against 10,000,000 

import time
start_time = time.time()
for i in range(10000, 10000000):
    end_time = time.time()

    time_taken = end_time-start_time

print(time_taken) 

### Create a list with random values and sort the list in ascending order without using sort.

lst = [2,4,5,7,3,1,9,]


for i in range(0,len(lst)):
 pass
 for f in range(i+1, len(lst)):    
    if lst[i]>=lst[f]:
        lst[i],lst[f] = lst[f],lst[i]

print(lst)

## Generate numbers between 1000 and 10,000 and write only the numbers divisible by 7 .txt file

m = []
for i in range(1000,10000):
   if i% 7 == 0:
    
      m.append(i)
print(m)
      
