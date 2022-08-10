import pandas as pd
#import copy as copy
import matplotlib.pyplot as plt

Data = pd.read_csv("data.csv")
KiwiWeights = Data["Weight(kg)"].tolist()

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



# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)
    return array

data = [8, 7, 2, 1, 0, 9, 6,3]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
    
