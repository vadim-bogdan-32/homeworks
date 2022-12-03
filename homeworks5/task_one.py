# Алгоритм
# 1.Бесконечный цикл для ввода номера
# 2.Запросить мобильный номер пользователя
# 3.Провалидировать карту согласно требованиям
# 4.Если валидация не успешна вывести сообщения с ошибками в виде словапя
# 5.Спрашивать хочет ли выйти из программы


operators = {'1': 'A1', '2': 'MTC', '3': 'A1', '5': 'MTC', '6': 'A1',
             '7': 'MTC', '8': 'MTC', '9': 'A1'}
error = False

while True:
    result = {}
    users_input = input("Введите номер в международном формате:")

    if len(users_input) != 13:
        result['success'] = True
        result['description'] = "Номер должен содержать 13 символов"
        error = True

    if users_input[0] == '+':
        for char in users_input[1:]:
            if not char.isdigit():
                result['success'] = False
                result['description'] = "Номер должен начинаться знаком \
плюс и содержать только цифры"
                error = True
                break
    else:
        result['success'] = False
        result['description'] = "Номер должен начинаться со знака +"
        error = True

    if not error:
        country_code = users_input[1:4]
        if country_code == '375':
            mobile_code = users_input[4:6]
            if mobile_code == '44':
                result['operator'] = 'A1'
            elif mobile_code == '33':
                result['operator'] = 'MTC'
            elif mobile_code == '25':
                result['operator'] = 'life :)'
            elif mobile_code == '29':
                a1_mts_code = users_input[6]
                if a1_mts_code in operators.keys():
                    result['operator'] = operators[a1_mts_code]
                else:
                    result['success'] = False
                    result['description'] = "неизвестный оператор"
                    error = True
            else:
                result['success'] = False
                result['description'] = "неизвестный оператор"
            print(result)
        else:
            result['success'] = False
            result['description'] = "Неизвестная страна"
            error = True
    if error:
        print(result)
    else:
        result['success'] = True
        result['number'] = users_input
        print(result)

    exit_code = input("Хотите выйти из программы? (Y/n):")
    if exit_code in ('Y', 'y'):
        break
