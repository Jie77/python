"""
This program requires creating a function using
def , return, print, input, if, in keywords,
.append(), .pop(), .remove() list methods,
As well as other standard Python

This program takes string input and checks if that
string is in a list of strings
1) if string is in the list, it removes the first instance from list
2) if string is not in the list, the input gets appended to the list
3) if the string is empty, then the last item is popped from the list
4) if the list becomes empty, the program ends
5) if the user enters "quit" , then the program ends

program has 2 parts
program flow which can be modified to ask for
    specific type of item. This is the programmers choice.
    Add a list of fish, trees, books, movies, songs.... your choice.
    2)list-o-matic Function which takes arguments of a string and a list.
    The function modifies the list and returns a message as seen below.

example 1 input/output

look at all the animals ['cat', 'goat', 'cat']
enter the name of an animal: horse
1 instance of horse appended to list

look at all the animals ['cat', 'goat', 'cat', 'horse']
enter the name of an animal: cat
1 instance of cat removed from list

look at all the animals ['goat', 'cat', 'horse']
enter the name of an animal: cat
1 instance of cat removed from list

look at all the animals ['goat', 'horse']
enter the name of an animal:          (<-- entered empty string)
horse popped from list

look at all the animals ['goat']
enter the name of an animal:          (<-- entered empty string)
goat popped from list

Goodbye!

example 2

look at all the animals ['cat', 'goat', 'cat']
enter the name of an animal: Quit
Goodbye!
"""

arr = ['cat', 'goat', 'cat']

def printAll(arr):
    print("look at all the animals", end=" ")
    print(arr)


def findIndex(arr, str):
    for i in arr:
        if i == str:
            return arr.index(i)
    return -1
printAll(arr)
print("enter the name of an animal:", end=" ")
Input = input()
while Input != "Quit":
    index = findIndex(arr, Input)
    if index != -1:
        arr.pop(index)
        print("1 instance of "+Input+" removed from list")
    elif len(Input) == 0:
        Input = arr.pop()
        print(Input+" popped form list")
    elif index == -1:
        arr.append(Input)
        print("1 instance of "+Input+" appended to list")


    if len(arr) == 0:
        break
    printAll(arr)
    print("enter the name of an animal:", end=" ")
    Input = input()
print("GoodBye")
