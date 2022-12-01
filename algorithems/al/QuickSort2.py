# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:51:56 2022

@author: shahad mohammed
"""

# the function partition is going to take an array, a starting index (low) and an ending index (high)
def partition(array, low, high):
 #Then make the pivot element position. In our case, it is the last element
  pivot = array[high]
  # pointer outside our array this pointer will always point to the last element of the smaller elements
  i = low - 1
  
  #we have to iterate over the array and check if the element is smaller or larger than the pivot 
  #and then swap it with the first element of the larger elements.

  for j in range(low, high):
      #if the element is smaller than the pivot, then we have to swap it with the first element of the larger elements.
      #So, fisrt will increase the value of 'i' by 1 than do the swapping.
      #if the element is larger then do nothing
    if array[j] <= pivot:
      #So, we will use a variable to know the first element of the larger elements.
      #Before we need to swap the elements, we will increase its value to point the first element of the larger elements.
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
      
   #Swap the pivot with the first element of the larger elements.( put the pivot in its correct position)
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  #Return the index of the pivot, so we can then use this index to divide our array further into subarrays.
  return i + 1
 
# the function quick_sort is going to take an array, a starting index (low) and an ending index (high)

def quick_sort(array, low, high):
    #if at least we have more than one element in the array
    #we will continue breaking the array until the size of the array becomes 1 (until low < high)
  if low < high:
    pivot  = partition(array, low, high)
    #Again, repeat this process-Recursive call - to the subarrays from 'low' to 'piovt-1' (the smaller elements) and 'piovt+1' to 'high' (the greater elements),
    #Leaving the pivot element because that is already in the place.
    quick_sort(array, low, pivot  - 1)
    quick_sort(array, pivot  + 1, high)
 
   