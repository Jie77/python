cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai",
          "Mexico City", "São Paulo", "Hyderabad"]
# Using cities, iterate through the list using "for"/"in"
# sort into lists with "A" in the city name and
# without "A" in the name: a_city & no_a_city

a_city = []
no_a_city = []
for i in cities:
    if "A" in i.upper():
        a_city.append(i)
    else:
        no_a_city.append(i)
print(a_city)
print(no_a_city)
