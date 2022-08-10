from random import randint, random
from sortingScript import  selectionSort
from time import time
 
averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)

 

# #SelectionSort   
def test_selectionWorst():
    start= time()
    assert selectionSort(worstcase, len(worstcase)) == bestcase
    print(time()-start)
 
def test_selectionBest():
    start= time()
    assert selectionSort(bestcase,len(bestcase)) == bestcase
    print(time()-start)
 
def test_selectionAvg():
    start= time()
    assert selectionSort(averagecase, len(averagecase)) == bestcase
    print(time()-start)



