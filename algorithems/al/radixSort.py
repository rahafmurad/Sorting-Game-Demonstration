# -*- coding: utf-8 -*-
"""
Created on Thu May 12 00:06:46 2022

@author: night
"""


# Using counting sort to sort the elements in the basis of significant places, takes array and the sigfig placement
def countingSort(array, place):
    size = len(array) #  identify the size of the array
    output = [0] * size # has the same amount of elemnts as the array 
    count = [0] * 10 # the array that counts the occarnce of each visit , with the base of 10, each element can be from 0 to 9

    # Calculate count of elements
    for i in range(0, size): # will - and then put accourdingly in the count array
        index = array[i] // place # // integer divison, cut the digit from righy by the number of zeros
        count[index % 10] += 1 # (index % 10,) gets 1 digit from right, the last digit

    # Calculate cumulative count/freqauncy
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1 # start from the last elemnt of the array
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1 # decrease index
        i -= 1 # to ittrate 

    # put each element in the passed array
    for i in range(0, size):
        array[i] = output[i] # putting all the elements in the output array
    print(array) # to see each pass for the elements 


# Main function to implement radix sort function
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0: # insures the number of passes
        countingSort(array, place)
        place *= 10 #  increase the placemnt, 1, 10, 100 etc..
        
        
numbers = [121, 432, 564, 23, 1, 45, 788]
radixSort(numbers)
print(numbers)
