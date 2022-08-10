from random import randint, random
from sortingScript import  quickSort
from time import time
 
averagecase= [4, 5, 1, 2, 3]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)
 

 
#  QuickSort
def test_quickSortWorst():
    start= time()
    L=worstcase
    assert quickSort(L,0,len(L)-1) == bestcase
    print(time()-start)
 
def test_quickSortBest():
    start= time()
    L=bestcase
    assert quickSort(L,0,len(L)-1) == bestcase
    print(time()-start)
 
def test_quickSortAvg():
    start= time()
    L=averagecase
    assert quickSort(L,0,len(L)-1) == bestcase
    print(time()-start)