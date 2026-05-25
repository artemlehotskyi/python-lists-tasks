languages = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]

print("Початковий список:", languages)

print("До sorted():   ", languages)
sorted_copy = sorted(languages)
print("Після sorted():", sorted_copy)
print("Оригінал не змінився:", languages)

print("До reverse():  ", languages)
languages.reverse()
print("Після reverse():", languages)

print("До sort():     ", languages)
languages.sort()
print("Після sort():  ", languages)
