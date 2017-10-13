my_str = "hello there"
print (my_str.isalpha())
# result is False

print ("Mississippi".replace('i','z',2))
# result is Mzsszssippi

print ('test'.center(10,'x'))
# result is xxxtestxxx

print ("NO".join("test"))
# result is tNOeNOsNOt

x= "test".join(["A","B","C"])
print (x)
# result is AtestBtestC

x="hello are you there"
print (x.split())
# result is ['hello', 'are', 'you', 'there']

my_str = "hello hello"
print (my_str.split('l'))
# result is ['he', '', 'o he', '', 'o']

x="frequency of letters"
print (x.split("e",2))
# result is ['fr', 'qu', 'ncy of letters']
