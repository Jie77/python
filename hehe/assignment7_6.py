"""
Implement the merge sort
Merge takes an unsorted list of numbers and returns
a sorted list. It does this by first splitting the
incoming list into two lists, the left and the right,
and sorting them individually using merge.
So, it first recursively breaks down the list until
each list has only one item;
a one-item list is guaranteed to be sorted.
Then, once it can guarantee that the left and right
are both sorted, it repeatedly compares the first
item from left to the first item from right.
Whichever is lower gets added to the final sorted list.
Once both left and right are empty, it returns
the newl sorted list. That newly sorted list is then
used in a previous call to Merge.
"""


import random

def merge(left, right):
    new = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    if i == len(left):
        for p in right[j:]:
            new.append(p)
    else:
        for p in left[i:]:
            new.append(p)
    return new

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr)//2
    left = mergeSort(arr[:pivot])
    right = mergeSort(arr[pivot:])
    return merge(left, right)



def rand(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 20))
    return arr

arr = rand(10)
new = mergeSort(arr)

print(arr)
print(new)
