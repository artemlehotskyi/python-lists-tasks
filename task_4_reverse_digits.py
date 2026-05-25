line = input("Введіть 5 цифр через пропуск: ")

digits = line.split()

reversed_digits = digits[::-1]

number_str = "".join(reversed_digits)
number = int(number_str)

print("Початковий список:", digits)
print("Зворотній список: ", reversed_digits)
print("Число:            ", number)
