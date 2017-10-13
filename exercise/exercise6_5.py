"""len(), .find()
len(working_string)
.find("i")
.find("i",start)
.find("i", start, end)
"""
# [ ] find and display the length of the string: topic
topic = ".len() returns the length of a string"
print(len(topic))
# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"
print(topic[:len(topic)//2])

# [ ] print index where first instance of the word  "code" starts using .find()
work_tip = "Good code is commented code"
print(work_tip.find("code"))

# [ ] search for "code" in work_tip using .find()
# [ ] save result in variable: code_index
# [ ] display index of where "code" is found, or print "not found" if code_index == -1

code_index = []
index = work_tip.find("code")
code_index.append(index)
start = 0
while index != -1:
    start = index + 1
    index = work_tip.find("code",start)
    code_index.append(index)
print(code_index[:len(code_index)-1])
