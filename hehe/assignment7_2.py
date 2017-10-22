"""
NOTE: This program requires print, input, def, return, for/in keywords,
.lower() and .upper() method, .append, .pop, .split methods,
range and len functions.

This program takes string input and then prints out a mixed order version of the string

Program Parts

1) program flow gathers the word list, modifies the case and order, and prints
    a) get string input, input like a poem, verse or saying
    b) split the string into a list of individual words
    c) determine the length of the list
    d) Loop the length of the list by index number and for each list index:
        i) if a word is short (3 letters or less) make the word in the list lowercase
        ii) if a word is long (7 letters or more) make the word in the list uppercase
    e) call the word_mixer function with the modified list
    f) print the return value from the word_mixer function

2) word_mixer Function has 1 argument: an original list of string words,
containing greater than 5 words and the function returns a new list.

    a) sort the original list
    b) create a new list
    c) Loop while the list is longer than 5 words:
        i) in each loop pop a word from the sorted original list
            and append to the new list
        ii) pop the word 5th from the end of the list and append to the new list
        iii) pop the first word in the list and append to the new list
        iv) pop the last word in the list and append to the new list
    d) return the new list on exiting the loop

input example (beginning of William Blake poem, "The Fly")
enter a saying or poem:
Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?

output example:
or BRUSHED thy not Little thou me? SUMMER’S thee? like THOUGHTLESS play i a not hand a my fly am man
"""
print("enter a saying or poem:")
Input = input()
arr = Input.split(" ")
length = len(arr)
for i in range(length):
    if len(arr[i]) <= 3:
        arr[i] = arr[i].lower()
    if len(arr[i]) >= 7:
        arr[i] = arr[i].upper()


def word_mixer(arr):
    arr.sort()
    new = []
    while len(arr) > 5:
        new.append(arr.pop(len(arr)-5))
        new.append(arr.pop(0))
        new.append(arr.pop())

    return new

print(' '.join(word_mixer(arr)))


