# Write a function that accepts a string of words separated
# by spaces consisting of alphabetic characters and
# returns a string such that each word in the input string
# is reversed while the order of the words in the input string is preserved.
# The length of the input string must be equal to the length of the output string
# i.e. there should be no extra trailing or leading spaces in your output string.
# For example if: input_string   = “this is a sample test”
# then the function should return a string such as: "siht si a elpmas tset"

input_string = input()

def reverse(str):
    return str[::-1]

def exchange(input_string):
    list = input_string.strip().split(' ')
    res = []
    for i in list:
        res.append(reverse(i))
    return ' '.join(res)

print(exchange(input_string))
