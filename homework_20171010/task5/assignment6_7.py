"""
In this assignment you are asked to write a spell checker (corrector).
This assignment includes 3 parts.

In the first part you are asked to write a function to compare two strings and
return 0 if they match,
return 1 if they mismatch in one character and
return 2 if they mismatch by more than one character.

In the second part you are asked to write a function to
check if a string can match another string by either
inserting or deleting a character.

In the third part you are asked to write a function to
correct spelling of a string (sentence) by using a list of correct words.
This third function uses the first two functions as helper functions.
"""

"""
Part1 :
Write a function named find_mismatch that accepts two strings 
as input arguments and returns:

0 if the two strings match exactly.
1 if the two strings have the same length and mismatch in only one character.
2 if the two strings do not have the same length or mismatch in two or more characters.

Capital letters are considered the same as lower case letters. 
Here are some examples:
First string	Second String	    Function return
    Python	         Java	        2
    Hello There   	  helloothere  1
    sin	             sink	        2 (note not the same length)
    dog	             Dog	        0
"""
# Type your code here


def find_mismatch(str1, str2):
    if len(str1) != len(str2):
        return 2
    flag = 0
    for i in range(len(str1)):
        if str1[i].lower() != str2[i].lower():
            flag += 1
            if flag >= 2:
                return 2
    return flag

# print(find_mismatch('Python','Java'))
# print(find_mismatch('Hello There','helloothere'))
# print(find_mismatch('sin','sink'))
# print(find_mismatch('Dog','dog'))

"""
Part 2:
Write a function named single_insert_or_delete that 
accepts two strings as input arguments and returns:

0 if the two strings match exactly.
1 if the first string can become the same as the second string 
by inserting or deleting a single character. 
Notice that inserting and deleting a character is not 
the same as replacing a character.
2 otherwise 
Capital letters are considered the same as lower case letters. Here are some examples:
First string	Second String	Function return
    Python	       Java	          2
    book	       boot	          2
    sin	           sink	          1 (Inserting a single character at the end)
    dog	            Dog	          0
    poke	       spoke	      1 (Inserting a single character at the start)
    poker	       poke	          1 (Deleting a single character from the end)
    programing	   programming	  1 (Inserting a single character)
"""
# Type your code here


def single_insert_or_delete(str1, str2):

    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i].lower() != str2[i].lower():
                return 2
        return 0
    elif abs(len(str1) - len(str2)) > 1:
        return 2
    else:
        temp = ""
        if len(str1) < len(str2):
            temp = str2
            str2 = str1
            str1 = temp
        obj = {}
        for i in str1:
            obj[i] = 0
        for j in str2:
            if j in obj:
                obj[j] = obj[j] + 1
        num = 0
        for i in obj:
            if obj[i] == 0:
                num = num+1
                if num > 1:
                    return 2
        return 1

# print(single_insert_or_delete('Python','Java'))
# print(single_insert_or_delete('book','boot'))
# print(single_insert_or_delete('sin','sink'))
# print(single_insert_or_delete('dog','Dog'))
# print(single_insert_or_delete('poke','spoke'))
# print(single_insert_or_delete('poker','poke'))
# print(single_insert_or_delete('programing','programming'))

"""
Part 3:
Write a function named spelling_corrector that accepts two arguments. 
The first argument is a sentence (string) and 
the second argument is a list of words (correct_spells). 
Your function should check each word in the input string 
against all the words in the correct_spells list and 
return a string such that:

1) If a word in the original sentence matches exactly with 
    a word in the correct_spells then the word is not modified 
    and it should be directly copied to the output string.
2) if a word in the sentence can match a word in the correct_spells list by 
    replacing, inserting, or deleting a single character, 
    then that word should be replaced by the correct word in the correct_spelled list.
3) If neither of the two previous conditions is true, 
    then the word in the original string should not be modified 
    and should be directly copied to the output string.

Notes:
    * Do not spell check one or two letter words (copy them directly to the output string).
    * In case of a tie use the first word from the correct_spelled list.
    * Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
    * All characters in the output string should all be in lower case letters.
    * Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
    * Remove extra spaces between the words.
    * Remove spaces at the start and end of the output string.
Examples:
    Sentence (str)	                  correct_spells (list)	                              Function return (str)
    Thes is the Firs cas	          ['that','first','case','car']	                         thes is the first case
    programing is fan and eesy	   ['programming','this','fun','easy','book' ]	         programming is fun and easy
    Thes is vary essy	              ['this', 'is', 'very', 'very', 'easy']	             this is very easy
    Wee lpve Pythen	              ['we', 'Live', 'In', 'Python']	                      we live python
Notice:
    * In the first example 'thes' is not replaced with anything.
    * In the first example both 'case' and 'car' could replace the 'cas' in the original sentence, but 'case' is selected because it was encountered first.

Please notice that this assignment is only an exercise and 
a real spell checker requires more functionalities.
Hint: You should use the functions that you developed in part 1 and part 2 
to help you solve this problem.
"""
# Type your code here
def not_empty(s):
    return s and s.strip()

def spelling_corrector(str, array):
    arr = str.split(' ')
    arr = list(filter(not_empty,arr))
    res = []
    for i in arr:
        flag = 1
        for j in array:
            if find_mismatch(i,j) == 0:
                flag = 0
                res.append(i.lower())
                break
            elif find_mismatch(i,j) == 1 or single_insert_or_delete(i,j) == 1:
                flag = 0
                res.append(j.lower())
                break
        if flag:
            res.append(i.lower())
    return ' '.join(res)

print(spelling_corrector("Thes is the Firs cas",['that','first','case','car']))
print(spelling_corrector("programing is fan and eesy",['programming','this','fun','easy','book' ]))
print(spelling_corrector("Thes is vary essy",['this', 'is', 'very', 'very', 'easy']))
print(spelling_corrector("Wee lpve Pythen",['we', 'Live', 'In', 'Python']))
