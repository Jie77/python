# Write a program using while loops that
# asks the user for a positive integer 'n'
# and prints a triangle using numbers from 1 to 'n'.
# For example if the user enters 6 then the output
# should be like this :
"""
1
22
333
4444
55555
666666
"""
# Type your code here

n = int(input())

for i in range(n):
    num = i + 1
    sum = num
    while i:
        sum = sum*10+num
        i = i - 1
    print(sum)


