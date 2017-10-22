# Write a function that accepts two positive
# integers a and b (a is smaller than b) and
# returns a list that contains all the odd numbers
# between a and b (including a and including b if applicable) in descending order.

def printOdd(a, b):
    arr = []
    if b%2 == 1:
        for i in range(b, a-1, -2):
            arr.append(i)
    else:
        for i in range(b-1, a-1, -2):
            arr.append(i)
    return arr

print(printOdd(3, 10))
print(printOdd(3, 11))
print(printOdd(2, 10))
print(printOdd(2, 11))
