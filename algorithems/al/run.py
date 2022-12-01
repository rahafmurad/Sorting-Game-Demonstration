# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 01:52:48 2022

@author: shahad mohammed
"""

# -*- coding: utf-8 -*-
#from RandomNumberss import*
import bisect
import time
import QuickSort2
import merageSort
import SelectAlgorithm
import radixSort



def readflist():
    my_file=open("RandomNumbersRead.txt","r")
    numbers=[]
    for number in my_file:
        numbers.append(int(number))
        
    my_file.close()
    return numbers

def write():
    writeCodeIn = open("RandomNumbersWrite.txt","w")

    for i in range(n):
        writeCodeIn.write(str(numbers[i])+"\n")
        
    writeCodeIn.close() 
  

numbers=readflist() 
n = len(numbers)  

start = time.process_time()
#QuickSort2.quick_sort(numbers,0, n - 1)
#merageSort.mergeSort(numbers)
#SelectAlgorithm.selectionSort(numbers)
radixSort.radixSort(numbers)
print("Time :" ,time.process_time()-start)
write()

