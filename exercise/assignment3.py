"""
This program requires print output and using code syntax:
if, input, def, return, for/in keywords,
.lower() and .upper() method, .append, .pop, .split methods, range and len functions

This program takes string input and then prints out a mixed order version of the string
program flow gathers the word list, modifies the case and order, and prints
    get string input, input like a poem, verse or saying
    split the string into a list of individual words
    determine the length of the list
    Loop the length of the list by index number and for each list index:
        if a word is short (3 letters or less) make the word in the list lowercase
        if a word is long (7 letters or more) make the word in the list uppercase
    call the word_mixer function with the modified list
    print the return value from the word_mixer function

word_mixer Function has 1 argument:
an original list of string words,
containing greater than 5 words and the function returns a new list.
    sort the original list
    create a new list
    Loop while the list is longer than 5 words:
        in each loop pop a word from the sorted original list and append to the new list
        pop the word 5th from the end of the list and append to the new list
        pop the first word in the list and append to the new list
        pop the last word in the list and append to the new list
        return the new list on exiting the loop

input example (beginning of William Blake poem, "The Fly")
enter a saying or poem:
Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?

output example:
or BRUSHED thy not Little thou me? SUMMER’S thee? like THOUGHTLESS play i a not hand a my fly am man
"""
