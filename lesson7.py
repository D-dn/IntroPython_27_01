# Генератор словарей

ascii_table = {numb: chr(numb) for numb in range(ord("A"), ord("D") + 1)}

print(ascii_table)

for key in ascii_table:  # Цикл всегда идет через ключи
    print(key, ascii_table[key])

print("A" in ascii_table) # Оператор in проверяет ключи
test_key = 67

value = ascii_table.get(test_key, "")

value = ''
if test_key in ascii_table:
    value = ascii_table[test_key]
print(value, type(value))

new_dict = ascii_table.copy()
new_dict["test"] = "test"
print(new_dict)
print(ascii_table)

for key, value in ascii_table.items():
    print(key, value)

print(ascii_table.items())
print(list(ascii_table.keys()))
print(list(ascii_table.values()))
ascii_table.pop(65) # удаление по ключу
ascii_table.popitem()
print(ascii_table)

dict_1 = {1: 1, 2: 2}
dict_2 = {2: "22", 3: "33"}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

# dict_3 = dict_1.update(dict_2)  # ошибка

dict_3 = {**dict_2, **dict_1}

print(dict_3)
print(dict_1, dict_2)




