with open('file_1.txt', 'r') as f:
    letter = input("Введите букву для нахождения числа её вхождений в файл:")
    text = f.read()
    new_text = text.casefold()
    qauntity = new_text.count(letter)

    print(qauntity)
