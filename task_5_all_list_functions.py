professions = ["teacher", "doctor", "engineer", "artist", "chef"]
print("Початковий список:", professions)

print("Довжина (len):", len(professions))

from_tuple = list(("pilot", "writer"))
print("list() з кортежа:", from_tuple)

print("Перший:", professions[0])
print("Останній:", professions[-1])

nested = [professions, from_tuple]
print("Список списків:", nested)
print("Елемент [0][1]:", nested[0][1])

professions[0] = "scientist"
print("Після зміни [0]:", professions)

print("Зріз [1:4]:", professions[1:4])
print("Зворотній порядок (зріз):", professions[::-1])

professions.append("musician")
print("Після append:", professions)

combined = professions + ["dentist"]
print("Після +:", combined)
professions.extend(["nurse", "actor"])
print("Після extend:", professions)

del professions[0]
print("Після del [0]:", professions)
professions.remove("artist")
print("Після remove('artist'):", professions)
popped = professions.pop()
print("pop() повернув:", popped, "| список:", professions)

print("'chef' in professions:", "chef" in professions)
print("'pirate' not in professions:", "pirate" not in professions)

professions.append("chef")
print("count('chef'):", professions.count("chef"))

professions.sort()
print("Після sort():", professions)
print("sorted() копія (reverse=True):", sorted(professions, reverse=True))

professions.reverse()
print("Після reverse():", professions)

numbers = list(range(1, 6))
print("list(range(1, 6)):", numbers)
print("sum:", sum(numbers), "| min:", min(numbers), "| max:", max(numbers))

oceans = ("Pacific", "Atlantic", "Indian", "Arctic", "Southern")
print("Кортеж океанів:", oceans)
print("Довжина кортежа:", len(oceans))
print("Перший океан:", oceans[0])
