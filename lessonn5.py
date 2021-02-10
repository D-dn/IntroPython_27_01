# sort, sorted

ages = [12, 34, 23, 55, 11, 4]

ages_sort = ages.copy()
ages_sort.sort()

ages_sort = sorted(ages)

print(ages, ages_sort)

value = ages.sort()
print(">>>>", value)

value = "342abc51QW+=/"

print(ord("="), ord("a"))
print(chr(61), chr(98))

value = ["Name", "Age", "Age_1", "address"]

res = sorted(value, reverse=False, key=len)

print(res)













my_str = 'blablacar'
my_symbol = "bla"


"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
2
"""
count = my_str.count(my_symbol)
print(count)



"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
for _ in range(count):
    print(my_symbol)
print('--------------------------------')

# responce = (my_symbol + "\n") * count
responce = f"{my_symbol}\n" * count
print(responce.strip())
print('--------------------------------')




"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA car"
my_str = my_str.lower()

result = []
result_str = ''

for symbol in my_str:
    if symbol not in result_str:
        result_str += symbol
        # result.append(symbol)
print(result_str)





"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
# my_str = "kdfgajfkshdfkhdbzvzxb siudf   ksdh"
# my_list = []
# print(my_list, id(my_list))

# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# print(my_list, id(my_list))

# my_list.extend(list(my_str)[::2])
# print(my_list, id(my_list))





"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
my_str = "kdfgajfkshdfkhdbzvzxb siudf   ksdh"
# print(len(my_str))
str_index = [2, 23, 30, 12, 3, 0, 33]
my_list = []
for index in str_index:
    value = my_str[index]
    my_list.append(value)
print(my_list)





"""
6)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и 
my_list_2 через один, начиная с my_list_1.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""








"""
7)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить 
элементы на четных местах из my_list_1, 
а потом все элементы на нечетных местах из my_list_2.
"""

my_list_1  = [1, 2, 3, 4, 5]
my_list_2 = [10, 20, 30, 40]
result = []
print(id(result))

result = my_list_1[::2] + my_list_2[1::2]
print(id(result))

result += my_list_1[::2]
result += my_list_2[1::2]
print(id(result), result)



"""
8)
Дано целое число (int). Определить сколько цифр в этом числе.
"""
number = 1827283583268523452834658925237827583752034773756836839
res = len(str(number))
print(res)


"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""
res = max(str(number))
print(res)


"""
10)
Дано целое число. Составить число с цифрами в обратном порядке.
"""
number = int(str(number)[::-1])
print(number)
"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""
sort_numb_symb = sorted(str(number))
number = int("".join(sort_numb_symb))
print(number)

