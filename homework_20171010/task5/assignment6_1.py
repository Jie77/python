""" Create a program inputs a phrase (like a famous quotation)
and prints all of the words that start with h-z

Sample input:
enter a 1 sentence quote, non-alpha separate words:
Wheresoever you go, go with all your heart
Sample output:
WHERESOEVER
YOU
WITH
YOUR
HEART
"""
# This program requires print output and using code syntax
# such as keywords for/in (iteration), input, if, else,
# .isalpha() method, .lower() or .upper() method


# hints:
    # split the words by building a placeholder variable: word
        # loop each character in the input string
        # check if character is a letter
        # add a letter to word each loop until a non-alpha char is encountered
# if character is alpha
    # add character to word
    # non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to else
# else
    # check if word is greater than "g" alphabetically
        # print word
        # set word = empty string
    # or else
        # set word = empty string and build the next word
# Consider how you will print the last word
# if it doesn't end with a non-alpha character
# like a space or punctuation?


#str = "Wheresoever you go, go with all your heart"
str = input()
str = str.strip()
quote = ""
for i in str:
    if i.isalpha() or i ==" ":
        quote += i.upper()
start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start = space_index + 1
    space_index = quote.find(" ",start,len(quote))
print(quote[start:])
