def if_even_one_intersection(num):
    """Функция определения четности числа
    Плюсы: наименьшее число операций
    Минусы: алгоритм расчета четности числа может показаться неявным

    >>> if_even_recursive(0)
    True
    >>> if_even_recursive(5)
    False
    >>> if_even_recursive(-10)
    True
    """
    return not num & 1


def if_even_plain(num):
    """Функция определения четности числа
    Плюсы: трациционный и явный алгоритм расчета четности числа,
    Минусы: чуть большее число операций, чем в предыдущем примере

    >>> if_even_recursive(0)
    True
    >>> if_even_recursive(5)
    False
    >>> if_even_recursive(-10)
    True
    """
    return num % 2 == 0


def if_even_recursive(num):
    """Функция определения четности числа
    Минусы: занимает больший объем памяти,
    т.к должна сохранять состояние вложенных вызовов
    Также число вызовов зависит от значения аргумента функции.
    Их число будет равно num // 2

    >>> if_even_recursive(0)
    True
    >>> if_even_recursive(5)
    False
    >>> if_even_recursive(-10)
    True
    """
    if num == 0:
        return True
    elif num == 1:
        return False
    elif num > 0:
        return if_even_recursive(num - 2)
    else:
        return if_even_recursive(num + 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
