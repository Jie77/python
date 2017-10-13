import random
import sys
import datetime
sys.setrecursionlimit(1000000)

def rand(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,100))
    return arr


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            [arr[i], arr[j]] = [arr[j], arr[i]]
    [arr[i+1], arr[r]] = [arr[r], arr[i+1]]
    return i+1
arr = rand(20000)

# arr = []
# for i in range(20000, 0, -1):
#     arr.append(i)
# print (arr)
start = datetime.datetime.now()
quicksort(arr, 0, len(arr)-1)
end = datetime.datetime.now()
print (end-start)
