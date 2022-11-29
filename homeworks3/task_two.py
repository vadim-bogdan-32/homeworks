# вывести строку в обратной порядке
str_two_words = input("Введите строку состоящую из двух слов: ")

list_str = str_two_words.split()
list_str.reverse()
result_str = " ".join(list_str)
print(result_str)
