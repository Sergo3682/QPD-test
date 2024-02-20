#!/usr/bin/python3

number = 1
max_nums = ''
max_sum = 0

while(int(number) != 0):
    cur_sum = 0
    number = input('Enter a decimel number:\n')
    for digit in number:
         if digit != '-':
            cur_sum += int(digit)
    if cur_sum == max_sum:
        max_nums += number + ' '
    elif cur_sum > max_sum:
        max_sum = cur_sum
        max_nums = number + ' '

print(f'The maximum sum of digits is {max_sum}\n\
List of numbers with this maximum sum of digits: {max_nums}')

