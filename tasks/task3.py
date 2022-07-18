import random
import timeit
import numpy as np
from random import randint


def quick_sort(list_to_sort: list):
    """среднее время: O(N*logN)
    худшее время: O(N^2)
    память: O (log n)
    Быстрая сортировка(Тони Хоара). Выполняется на прямом ходу рекурсии.

    Плюсы: работает быстрее для небольших наборов данных,
    требуется меньшее пространство памяти по сравнению с сортировкой слиянием
    Минусы: O(N^2) - худшее время
    """
    less = []
    equal = []
    greater = []
    if len(list_to_sort) > 1:
        pivot = list_to_sort[0]
        for i in list_to_sort:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        less = quick_sort(less)
        greater = quick_sort(greater)
        list_to_sort = less + equal + greater
    return list_to_sort   # при len(list_to_sort) <= 1 базовый случай


def merge_two_list(list1: list, list2: list):
    """Алгоритм слияния двух отсортированных списков.
    Используется при реализации алгоритма сортировки слиянием.
    """
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    if i < len(list1):
        merged_list += list1[i:]
    if j < len(list2):
        merged_list += list2[j:]
    return merged_list


def merge_sort(list_to_sort: list):
    """время: O(N*logN)
    память: O (N)
    Сортировка слиянием. Выполняется на обратном ходу рекурсии

    Минусы: требуется дополнительное пространство памяти
    Плюсы: Алгоритм сортировки слиянием работает одинаково и точно
    независимо от количества элементов
    """
    if len(list_to_sort) == 1:  # базовый случай
        return list_to_sort
    middle = len(list_to_sort) // 2
    left = merge_sort(list_to_sort[:middle])
    right = merge_sort(list_to_sort[middle:])
    return merge_two_list(left, right)


def print_stats(list_to_sort: list, message: str):
    """Печатает данные о времени сортировки в мс.
    списка list_to_sort алгоритмами: быстрая сортировка, слиянием

    :param list_to_sort: список информация о сортировке которого выводится
    :param message: информационное сообщение, которое печатается в начале
    :return: None
    """
    print('\n' + message)
    algorithms = [merge_sort, quick_sort]
    max_len_name = max(algorithms, key=lambda x: len(x.__name__))
    print(
        ' ' * (len(max_len_name.__name__))
        + ' min  ' + 'max  ' + 'med  ' + 'ave'
    )
    for sorting in algorithms:
        test = timeit.Timer(lambda: sorting(list_to_sort))
        result = test.repeat(repeat=1000, number=1)

        print(
            sorting.__name__,
            round(np.amin(result)*1000, 2),
            round(np.amax(result)*1000, 2),
            round(np.median(result)*1000, 2),
            round(np.average(result)*1000, 2)
          )


if __name__ == "__main__":
    a = [i//10 for i in range(1, 100)]
    random.shuffle(a)
    print_stats(a, 'randomised array with limited values')

    a = [randint(0, 100) for i in range(100)]
    print_stats(a, 'randomised array')

    a = [i for i in range(100)]
    print_stats(a, 'already sorted array')

    a = [i for i in range(100, -1, -1)]
    print_stats(a, 'reversed sorted array')
