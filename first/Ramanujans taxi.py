num = input()
arr = []
for i in range(1,13):
    for j in range(1,13):
        if (i**3+j**3)==int(num):
            arr.append(i)
arr = list(set(arr))
print(arr)
