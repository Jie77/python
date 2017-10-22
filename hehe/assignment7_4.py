"""
Implement the bubble sort:
Write a function that accepts a list of integers and
returns a new list which is the sorted version (ascending order)
of the original list (Original list should not be modified).
You may NOT use the built in sort() or sorted() functions.
Notice that the original list should not be modified
"""
import random
def bubbleSort(arr):
    new = []
    for i in arr:
        new.append(i)
    for i in range(len(new)-1):
        for j in range(len(new)-i-1):
            if new[j] > new[j+1]:
                new[j], new[j+1] = new[j+1], new[j]
    return new

def rand(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 20))
    return arr

arr = rand(10)
new = bubbleSort(arr)

print(arr)
print(new)
