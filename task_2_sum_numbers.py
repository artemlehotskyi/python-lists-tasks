line = input("Введіть числа через пропуск: ")

parts = line.split()

total = 0
for part in parts:
    total = total + int(part)

print("Сума:", total)
