a = 10  # int
print(a, type(a))

a = 1.0  # float
print(a, type(a))

a = "10"  # str
print(a, type(a))

a = 2
b = 3
c = a + b
a = c * b
b = a - b - c
print(b)

number_1 = 10  # int
print(number_1, type(number_1))

number_float = 1.0  # float
print(number_float, type(number_float))

age_str = "10"  # str
print(age_str, type(age_str))

test_value = 2
print(test_value)

my_str = input("Введи строку: ")
my_number = input("Введи целое число: ")
my_number = int(my_number)
# print(type(my_number))
result = my_str * my_number
print(result)

str_ = "-100.95"
value = float(str_)

print(value)
value = int(value)
print(value)

value = str(value)
print(value)



# bool  True/False

my_bool = 22 != 22

value = number = 5

print(str(my_bool))

test_value = "False"
print(bool(test_value))

value = bool("") or bool("")
print(value)

value = bool("qwe") and (bool("q") or bool(""))
print(value)
