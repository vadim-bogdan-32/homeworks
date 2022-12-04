index = int(input("Введите индекс числа Фибоначчи:"))

n0 = 0
n1 = 1

new_index = index + 1

for i in range(2, new_index):
    n2 = n0 + n1
    n0 = n1
    n1 = n2

print(n1)
