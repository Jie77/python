"""
Program: List of letters

Input a word string (word)
find the string length of word
use range() to iterate through each letter in word (can use to range loops)
Save odd and even letters from the word as lists
    odd_letters: starting at index 0,2,...
    even_letters: starting at index 1,3,...
print odd and even lists
# complete List of letters program- test with the word "complexity"
"""

odd_letters = []
even_letters = []
str = "complexity"
for i in str:
    if (str.index(i)+1)%2 == 0:
        even_letters.append(i)
    else:
        odd_letters.append(i)

print(odd_letters)
print(even_letters)
