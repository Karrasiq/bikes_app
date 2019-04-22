def is_name(name):
    try:
        if name.istitle():  # Первая буква заглавная, остальные неважно
            result = True
        else:
            result = False
    except TypeError:
        print('Неверный тип данных аргумента')
    except Exception as e:
        print('Что-то пошло не так. Класс ошибки ({})'.format(e.__class__))
    
    return result


def normalize_full_name(first_name='', last_name=''):
    if first_name and last_name:
        result = '{} {}'.format(first_name, last_name).title()
    elif first_name:
        result = '{}'.format(first_name).title()
    elif last_name:
        result = '{}'.format(last_name).title()
    else:
        result = ''
    
    return result


def increase_list(var1, var2, var3):
    return [var1 * 2, var2 * 2]


def filter_list(some_list):
    for i in some_list.copy():
        try:
            if i <= 0:
                some_list.remove(i)
        except TypeError:
            print(f'Элемент {i} не числовой и не может быть обработан')

    return some_list


def max_list(some_list, var1, var2):
    try:
        if var1 > var2:
            some_list.append(var1)
        elif var1 < var2:
            some_list.append(var2)
    except TypeError:
        print('2 и 3 аргументы несравнимы между собой')


def get_dictionary(key, value):
    return {key: value}


def set_dictionary(some_dict, key, value):
    return some_dict.update({key: value})


def swap_dictionary(some_dict):
    return {value: key for key, value in some_dict.items()}


def increase(some_int):
    return lambda another_int: another_int * some_int
