import random as rnd
# # from random import randint, choice, shuffle
#
# test_str = "qawerty"
# # func_dict = {0: type,
# #              1: len,
# #              2: max,
# #              3: min}
# #
# number = rnd.randint(1, 3)
# # value = func_dict[number](test_str)
# # print(number, value)
#
# rand_symbol = rnd.choice(test_str)
# print(rand_symbol)
#
# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# new_list = list(set(test_list))
# rnd.shuffle(test_list)
# print(new_list)
# print(test_list)

def test_fuction(param):
    print(param)


def test_fuction_2():
    value = rnd.randint(1, 10)
    return value



test_fuction("Hello, World!")
result = test_fuction_2()
print(result)