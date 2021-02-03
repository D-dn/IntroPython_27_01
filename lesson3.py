# форматирование строк

# my_str = "qwerty"
# print(f"my_str={my_str}")

path = "/home/vz/test"
filename = "python_test.py"
# full_path = path + "/" + filename

full_path = f"{path}/{filename}"
print(full_path)
print(len(full_path))

print(full_path[2:6]) # правый край не включается в срез
print(full_path[:6])
print(full_path[6:])
print(full_path[::2]) # на четных местах шаг 2
print(full_path[1::2])# на нечетных местах шаг 2
print(full_path[::-1])# разворот строки

# full_path = "{}/{}".format(path, filename)
# print(full_path)





# цикл while
# value = input("Введи что-то")
#
# if value:
#     print("OK")
# else:
#     value = input("Введи что-то")

# while not value:
#     value = input("Введи что-то")

# print("Ok")

# from random import randint
# goal = randint(1, 10)
#
# value = int(input("Угадай число"))
# done = False
#
# while not done:
#     if value > goal:
#         value = int(input("Попробуй меньше"))
#     elif value < goal:
#         value = int(input("Попробуй больше"))
#     else:
#         done = True # изменение состояния


# while True:
#     if value > goal:
#         value = int(input("Попробуй меньше"))
#     elif value < goal:
#         value = int(input("Попробуй больше"))
#     else:
#         break # выход из текущего цикла

# while value != goal:
#     if value > goal:
#         value = int(input("Попробуй меньше"))
#     else:
#         value = int(input("Попробуй больше"))

# print("Угадал!!!")













# Тернарный оператор

# value = int(input("Какая температура?"))
#
# if value >= 0:
#     result = 1
# else:
#     result = -1
#
# result = 1 if value >= 0 else -1
#
# print(result)


# if условие:
#     блок действий если условие Да
# elif условие2:
#     блок действий если условие2 Да
# .....
# else:
#     блок действий если Нет

# if 4 > 20:
#     print("4 > 2")
#
# value = int(input("Какая температура?"))
#
# if value < 0:
#     print("Надень шапку!")
# else:
#     print("Шапку можно не надевать ))")