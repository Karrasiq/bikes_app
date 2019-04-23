def is_name(name):
    try:
        if name.istitle():
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


def filter_list(list_to_filter):
    for i in list_to_filter.copy():
        try:
            if i <= 0:
                list_to_filter.remove(i)
        except TypeError:
            print(f'Элемент {i} не числовой и не может быть обработан')

    return list_to_filter


def max_list(list_to_extend, var1, var2):
    try:
        if var1 > var2:
            list_to_extend.append(var1)
        elif var1 < var2:
            list_to_extend.append(var2)
    except TypeError:
        print('2 и 3 аргументы несравнимы между собой')


def get_dictionary(key, value):
    return {key: value}


def set_dictionary(dict_to_extend, key, value):
    return dict_to_extend.update({key: value})


def swap_dictionary(dict_to_swap):
    return {value: key for key, value in dict_to_swap.items()}


def increase(multiplier):
    return lambda var_to_multiply: var_to_multiply * multiplier
