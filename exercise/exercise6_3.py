# get user input for first_name
first_name = input()
# create an empty string variable: new_name
new_name = ""
# iterate through letters in first_name
for i in first_name:
    if i == 'i' or i == 'o':
        i = i.upper()
    new_name = new_name + i
# add each letter in new_name
# capitalize if letter is an "i" or "o" *(hint: if, elif, else)
# print new_name

print(new_name)
