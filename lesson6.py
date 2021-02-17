# Словари dict key:value  key - неизменяемый объект, value - любой объект. Ключи - уникальные, значения могут повторяться.

# points = [[1, 2], [3, 4], [2, 6]]
# points[-1][0] = 10
# print(points)
#
# points = {"A": {"x": 1, "y": 2}, "B": {"x": 3, "y": 4}, "C": [2, 6]}
# points["B"]["y"] = 7
# print(points["B"])

# person = {"name": "John",
#           "age": 23,
#           "job": "lawyer",
#           "address": {"country": "USA",
#                       "city": "NY"}}
# person["sex"] = "male"
# person["age"] = 43
# person["age"] = 100
# print(person)

test_dict = {"test": [],
             "": "test?",
             12: "asd",
             10:1,
             None: "asd",
             False: 123,
             (1,2,3): [1,2,3],
             print: (1,2,3)}


print(test_dict)



# Множества set - уникальные элементы, порядок не гарантируется, объекты не изменяемые

# animals = ["dog", "cat", "dog", "dog", "cat", "rat", "monkey", "rat", (11, (1,2)), (11, 1)]
#
# new_set = set(animals)
#
# print(new_set, type(new_set))

# test_list = [(1,2,3), [1,2,3], (2,6), [1,80]]
# test_list = [tuple(my_item) for my_item in test_list]
# result_set = set(test_list)
# result_set.add((2,"6"))
# res = result_set.pop()
# print(res, result_set)

# set_1 = set()
# print(type(set_1))

# set_1 = {1, 2, 3, 4}
# set_2 = {3, 4, 5, 6}
# print(type(set_1))
#
# set_3 = set_2.union(set_1)
# print(set_1, set_2, set_3)
# set_4 = set_2.intersection(set_1)
# print(set_4)
# set_5 = set_2.difference(set_1)
# print(set_5)


# Генераторы списков
# number = 9

# result_list = []
# for numb in range(1, number + 1):
#     res_numb = numb ** 2
#     result_list.append(res_numb)

# result_list = [numb ** 2 for numb in range(1, number + 1)]
# print(result_list)
#
# test_str = "qwerty"
# res_str_list = [symbol * 2 for symbol in test_str if symbol not in "eyuioa"]
# print(res_str_list)


# a = 5
# b = 6
# tmp = b,a
# x, y = tmp
# print(x)

"""
6)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и
my_list_2 через один, начиная с my_list_1.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
# my_result = []
# my_list_1 = [10, 20, 30, 40, 50, 60, 70]
# my_list_2 = [1, 2, 3, 4, 5]
#
# list_len = min(len(my_list_1), len(my_list_2))
# # if len(my_list_2) < len(my_list_1):
# #     my_list_2, my_list_1 = my_list_1, my_list_2
#
# for index in range(list_len):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
#
# tail = my_list_2[list_len:] if len(my_list_2) > len(my_list_1) else my_list_1[list_len:]
# # my_result += tail
# my_result.extend(tail)
#
# print(my_result)
