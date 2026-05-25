cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']

first_part = ", ".join(cities[:-1])
last = cities[-1]

message = first_part + " and " + last

print(message)
