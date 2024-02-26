#!/usr/bin/python3

import re

validInputPattern = "^-?[0-9]+$"

def getNumber():
    isValid = False
    while not isValid:
        number = input('Enter an integer number:\n')
        if re.match(validInputPattern, number):
            isValid = True
        else:
            print(f'Invalid input. Please try again.')
    return number

number = 1
maxNums = ''
maxSum = 0

while(int(number) != 0):
    curSum = 0
    number = getNumber()
    for digit in number:
         if digit != '-':
            curSum += int(digit)
    if curSum == maxSum:
        maxNums += number + ' '
    elif curSum > maxSum:
        maxSum = curSum
        maxNums = number + ' '

print(f'The maximum sum of digits is {maxSum}\n\
List of numbers with this maximum sum of digits: {maxNums}')

