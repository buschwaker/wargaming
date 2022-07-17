import timeit
import numpy as np
from random import randint


def quick_sort(list_to_sort):
    """
    среднее время: O(N*logN)
    худшее время: O(N^2)
    память: O (log n)
    Выполняется на обратном ходу рекурсии
    Плюсы: работает быстрее для небольших наборов данных, требуется меньшее простанство памяти по сравнению с сортировкой слиянием
    Минусы: O(N^2) - худшее время, хуже работает с большими массивами данных
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
        more = quick_sort(greater)
        list_to_sort = less + equal + more
    return list_to_sort


def merge_two_list(list1, list2):
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


def merge_sort(s):
    """
    время: O(N*logN)
    память: O (N)
    Выполняется на прямом ходу рекурсии
    Минусы: требуется дополнительное пространство памяти
    Плюсы: Алгоритм сортировки слиянием
    работает одинаково и точно независимо от количества элементов
    """
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


a = [randint(1, 100) for i in range(1000)]
# b = [randint(0, 100) for i in range(100)]
#
# # a = [i for i in range(100)]
# # b = [i for i in range(100)]

# a = [i for i in range(100, -1, -1)]
# b = [i for i in range(100, -1, -1)]

print(a)
print(merge_sort(a))
print(a)
print(quick_sort(a))
print(a)

#
# merge_test = timeit.Timer(lambda: merge_sort(a))
# merge_result = merge_test.repeat(repeat=1000, number=1)
# print(np.amin(merge_result)*1000, np.amax(merge_result)*1000, np.median(merge_result)*1000, np.average(merge_result)*1000)
#
# quicktest = timeit.Timer(lambda: quick_sort(a))
# quickresult = quicktest.repeat(repeat=1000, number=1)
# print(np.amin(quickresult)*1000, np.amax(quickresult)*1000, np.median(quickresult)*1000, np.average(quickresult)*1000)