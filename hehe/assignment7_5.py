"""
Implement the selection sort:
Write a function that accepts a list of integers and
returns a new list which is the sorted version (dscending order)
of the original list (Original list should not be modified).
You may NOT use the built in sort() or sorted() functions.
Notice that the original list should not be modified.
"""

import random
def selectSort(arr):
    new = []
    for i in arr:
        new.append(i)
    for i in range(len(new)):
        k = i
        for j in range(i+1, len(new)):
            if new[k] > new[j]:
                k = j
        if k != i:
            new[k], new[i] = new[i], new[k]

    return new

def rand(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 20))
    return arr

arr = rand(10)
new = selectSort(arr)

print(arr)
print(new)

