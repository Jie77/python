"""
Write a program that asks the user for an input 'n'
(assume that the user enters a positive integer)
and prints only the boundaries of the triangle using
asterisks "*" of height 'n'.
For example if the user enters 6 then the height of
the triangle should be 6 as shown below and there
should be no spaces between the asterisks on the top line:
******
*   *
*  *
* *
**
*
"""
n = int(input())
for i in range(n):
    str = ''
    if i == 0:
        num = n
        while num:
           str += '*'
           num = num-1
    else:
        # num = n-i
        # str += '*'
        # for j in range(num-2):
        #     str += " "
        # str += '*'
        for j in range(n-i):
            if j == 0 or j == n-i-1:
                str += '*'
            else:
                str += ' '
    print(str)
