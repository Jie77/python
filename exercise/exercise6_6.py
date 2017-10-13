
# [ ]  count times letter "i" appears in code_tip string
"""
.count("i")
.count("i", start)
.count("i", start, end)
"""
# [ ] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
code_index = []
index = code_tip.find("i")
code_index.append(index)
start = 0
while index != -1:
    start = index + 1
    index = code_tip.find("i",start)
    code_index.append(index)
print(code_index[:len(code_index)-1])
print(code_tip.count('i'))
