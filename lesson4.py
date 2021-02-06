# обработка исключений

# цикл for
# кортежи
# списки

my_string = "test strIng"
my_string_2 = "test strIng".upper()
print(len(my_string))

for symbol in my_string:
    if symbol.lower() in "eyuioa" and symbol.isupper():
        print(symbol)

for index in range(len(my_string)):
    if not index % 2:
        print(index, my_string[index], my_string_2[index])

for index, symbol in enumerate(my_string):
    # print(index, symbol)
    if not index % 2:
        print(index, symbol)

# кортежи tuple

my_tuple = (1, 2, (3, 4), "123", 3.14, True, None) # неизменяемый тип

print(type(my_tuple), my_tuple)

print(my_tuple[1:4])

point = (2, 4, -7)
x_0 = point[0]
print(x_0)
x_0 += 2

point = (x_0, point[1], point[2])
print(point)


# списки list
my_list = [1, 2, (3, 4), "123", 3.14, True, None] # изменяемый тип

print(type(my_list), my_list)
print(my_list[0])

point = [2, 4, -7]
x_0 = point[0]
print(x_0)
x_0 += 2
point[0] = x_0
print(point)

my_tuple = list(my_tuple)
my_tuple[-1] = -1
my_tuple = tuple(my_tuple)

for value in my_list:
    if type(value) == str:
        print(value)

new_list = []

for number in range(1, 6):
    value = number ** 2
    new_list.append(value)


print(new_list)





# Обработка исключений

value = input("Введи целое число")
if value.isdigit():
    value = int(value)
    result = value / 2
else:
    print("Не верный ввод")
    result = ""
value = float(value)

try:
    value = float(value)
    result = 2 / value
except (ValueError, TypeError):
    print("Не верный ввод")
    value = 0
    result = 1
except ZeroDivisionError:
    print("Деление на 0")
    value = 0
    result = 1
except FileExistsError:
    pass
print(result)


# методы строк

my_str = "qwertyqwerty"
symbol = "ty"
# res = my_str.rfind(symbol)
# filename = filename.replace("jpeg", "jpg")
res = my_str.replace(symbol, "TY", 1)
print(res)

test_str = "qwerty is default String"

# res = test_str.capitalize()
res = test_str[0].upper() + test_str[1:]
print(res)
res = test_str.replace(test_str[0], test_str[0].upper(), 1)
print(res)

