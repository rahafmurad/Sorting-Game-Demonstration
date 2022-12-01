# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 04:31:43 2022

@author: rahaf
"""




def mergeSort(array):

    if len(array) > 1:  #check if the list have at least two number
        
        r = len(array)//2  #Divide the array into two pairs
        L = array[:r]        
        M = array[r:]
        print(L , M)
        mergeSort(L)      #Divide the array into pairs
        mergeSort(M)
 
        i = j = k = 0  #pointers

        while i < len(L) and j < len(M):   # Merge each pair in nondecreasing order
            if L[i] < M[j]:     #if L[i]< M[j]  add L[i] to array
                array[k] = L[i]
                i += 1          # move pointer of L to next index
            else:
                array[k] = M[j]   #if M[i]< L[j]  add M[i] to array
                j += 1            # move pointer of M to next index
            k += 1                 # move pointer of array to next index
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in the array
        while i < len(L):   
            array[k] = L[i]
            i += 1          # move pointer of L to next index
                    
            k += 1           # move pointer of array to next index

        while j < len(M):            
            array[k] = M[j]
            j += 1                     # move pointer of M to next index
            k += 1                     # move pointer of array to next index
                    
        return array

