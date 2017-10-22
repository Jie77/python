arr = ["cfvfvf","fvfdvafd","cadscasdca","ffafdfsd","cdcadcds","ffrrfrfvg"]

def find(arr):
    for i in range(len(arr)):
        if arr[i][0:1] == 'c':
            return i + 1
    return False

while find(arr):
    arr.pop(find(arr) - 1)

print(arr)


