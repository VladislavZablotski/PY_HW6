# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

list1 = [1, 8, 15, 4, 22, 34, 12, 48, 19]
# Принимаем диапазон 10...20
list_index = []
for i in range(len(list1)):
    if list1[i] in range(10,21):
        list_index.append(i)
print(list_index)
