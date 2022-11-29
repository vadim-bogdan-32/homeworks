# Сгенерировать список из 10 случайных элементов
# (чисел в диапазоне от -100 до 100)
# и вывести его на экран
# вставьте на 3-ю позицию новое случайное значение,
# удалите элемент из списка под индексом 6.выведите на экран новый список.
import random

list_one = []
for i in range(10):
    list_one.append(random.randrange(-100, 100))
print(list_one)
list_one[3] = random.randrange(-100, 100)
list_one.pop(6)
print(list_one)
