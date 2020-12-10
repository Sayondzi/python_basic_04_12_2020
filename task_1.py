a = 5

variable = input("Введите числовое значение от 0 до 10\n>>>")
if variable.isdigit():
    variable = int(variable)
else:
    print("Указано нечисловое  обозначение.")
    exit()

if 0 < variable < 10:
    b = a ** 3
    print(b)
else:
    b = 2 * a
    print(b)
