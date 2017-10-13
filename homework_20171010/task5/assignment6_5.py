"""
Write a function which accepts an input string and
returns a string where the case of the characters are changed,
i.e. all the uppercase characters are changed to lower case
and all the lower case characters are changed to upper case.
The non-alphabetic characters should not be changed.
Do NOT use the string methods upper(), lower(), or swap().
For exampe, if your string is "This is My FlowEr 21This"
the output should be "tHIS IS mY fLOWeR 21tHIS"
"""

#string = "This is My FlowEr 21This"
string = input()

def exchange(string):
    res = ""
    for i in string:
        if i.isalpha():
            if ord(i) <= 90:
                res += chr(ord(i)+32)
            else:
                res += chr(ord(i)-32)
        else:
            res += i
    return res
print(exchange(string))
