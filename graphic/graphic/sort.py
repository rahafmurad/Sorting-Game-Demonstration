# -*- coding: utf-8 -*-
from RandomNumberss1 import*
import bisect
import merageSort



"""
Created on Wed Apr 27 01:37:30 2022

@author: rahaf
"""

def readflist1():
    my_file=open("randomNumbers.txt","r")
    numbers=[]
    for number in my_file:
        numbers.append(int(number))
     
    my_file.close()
    return numbers

numbers=readflist1()
n = len(numbers)  

 
def write():
    writeCodeIn = open("RandomNumbersWrite.txt","w")

    for i in range(n):
        writeCodeIn.write(str(numbers[i])+"\n")
        
    writeCodeIn.close() 


        
merageSort.mergeSort(numbers)
write()
            
            
    

        