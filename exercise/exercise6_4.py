# Program: print each word in a quote
quote = "they stumble who run fast"

start = 0
space_index = quote.find(" ")
while space_index != -1:
    # code to print word (index slice start:space_index)
    print(quote[start:space_index])
    start = space_index + 1
    space_index = quote.find(" ",start,len(quote))
print(quote[start:])
