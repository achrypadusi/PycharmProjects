
import random
import time
from time import time
import numpy as np
from numpy import random as ranArr


def sortInsert(randomlist):
    sortedlist = randomlist.copy()
    i = 0
    sortedlist[i] = -1
    for unEl in randomlist:
        j = i
        sortedlist[j] = -1
        while j > 0:
            if randomlist[i] >= sortedlist[j-1]:
                sortedlist[j] = randomlist[i]
                break
            else:
                sortedlist[j] = sortedlist[j-1]
            j-=1
        if j == 0:
            sortedlist[j] = randomlist[i]
        i+=1
    return sortedlist


vecLen = int(input('number of cards:'))
startTime = time()
randomlist = random.sample(range(0,100000000),vecLen)
print ('Random Time: ',time()-startTime)

startTime = time()
randomArrayTest = ranArr.randint(100000000,size=(vecLen))
print ('Random Time Array: ',time()-startTime)

randomArray = np.array(randomlist)


startTime = time()
sorted1 = sorted(randomlist)
excTime = time()-startTime
print('sorted list: ', excTime)
#print (sorted1)

startTime = time()
arrSorted1 = np.sort(randomArray)
excTime = time()-startTime
print('sorted array: ', excTime)
#print(arrSorted1)

# startTime = time()
# sorted2 = sortInsert(randomlist)
# excTime = time()-startTime
# print('sort insert list: ', excTime)
#print(sorted2)