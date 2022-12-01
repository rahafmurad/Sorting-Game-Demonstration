# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 14:42:31 2022

@author: shahad mohammed
"""

import random

def generateRandomNumber():
    randomNumber = random.randint(1,100000)
    return randomNumber

def main():
    numberOfRandomNumbers = int(input("How many numbers "+\
                                      "should the random file hold?:"))

    fileToBeWrittenTo = open("randomNumbers.txt","w")

    for randomNumberCount in range(1, numberOfRandomNumbers + 1):
         randomNumber = generateRandomNumber()
         fileToBeWrittenTo.write(str(randomNumber)+"\n")

main()