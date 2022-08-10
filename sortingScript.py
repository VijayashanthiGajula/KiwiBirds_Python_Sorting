import pandas as pd
#import copy as copy
import matplotlib.pyplot as plt

Data = pd.read_csv("data.csv")
print("original data")
print (Data)

KiwiWeights = Data["Weight(kg)"].tolist()
#print("*******************original Kiwi Weights*******************")
#print(KiwiWeights) 


#*******************  Bubble Sort *********************8
def bubbleSort(Unsorted):
   #copy data into a new list
   List=Unsorted.copy()
   # Swap the elements to arrange in order
   for i in range(len(List)-1,0,-1):
      for j in range(i):
          if List[j]>List[j+1]:
            List[j], List[j+1] = List[j+1], List[j]     
   return List          
BubbleSortData=bubbleSort(KiwiWeights)
print("   ")
print("****************** bubble sort ***************")
print("   ")
print(BubbleSortData)
#****************** Bubble Sort ***************


#****************** Selection Sort ***************
def selectionSort(List, size):
      
      for i in range(size-1):
       min_index = i
       for j in range(i+1, size):
            # Update the min_index if the element at j is lower than it
            if List[j] < List[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
       List[i], List[min_index] = List[min_index], List[i]
      return List   
      
SelectionSortData=KiwiWeights.copy()  
size=len(SelectionSortData)
selectionSort(SelectionSortData,size)
print("   ")
print("****************** Selection sort ***************")
print("   ")
print(SelectionSortData)
#******************          Selection Sort              ***************

#****************** Quick Sort ***************
# function to find the partition position
def partition(List, low, high):
  # choose the rightmost element as pivot
  pivot = List[high]
  # pointer for greater element
  i = low - 1
  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if List[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      # swapping element at i with element at j
      (List[i], List[j]) = (List[j], List[i])
  # swap the pivot element with the greater element specified by i
  (List[i + 1], List[high]) = (List[high], List[i + 1])
  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(List, low, high): 
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(List, low, high)

    # recursive call on the left of pivot
    quickSort(List, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(List, pi + 1, high)
    return List
QuickSortData=KiwiWeights.copy()  

quickSort(QuickSortData, 0, len(QuickSortData) - 1)
print("   ")
print("****************** Quick Sort ***************")
print("   ")
print(QuickSortData)
 #****************** Quick Sort ***************