# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 02:07:35 2022

@author: rahaf
"""


import random


def generateRandomNumber():
    randomNumber = random.randint(1,10000000 )
    return randomNumber
 

def main():
    numberOfRandomNumbers = int(input("How many numbers "+\
                                      "should the random file hold?:"))

    fileToBeWrittenTo = open("randomNumbers.txt","w")

    for randomNumberCount in range(1, numberOfRandomNumbers + 1):
         randomNumber = generateRandomNumber()
         fileToBeWrittenTo.write(str(randomNumber)+"\n")

   
main()