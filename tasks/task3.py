import timeit
import numpy as np
from random import randint
from copy import deepcopy


def quick_sort(arr):
    """
    среднее время: O(N*logN)
    худшее время: O(N^2)
    память: O (log n)
    Плюсы: работает быстрее для небольших наборов данных, требуется меньшее простанство памяти по сравнению с сортировкой слиянием
    Минусы: O(N^2) - худшее время, хуже работает с большими массивами данных
    """
    less = []
    equal = []
    greater = []
    if len(arr) > 1:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        less = quick_sort(less)
        more = quick_sort(greater)
        arr = less + equal + more
    return arr


def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    """
    время: O(N*logN)
    память: O (N)
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



a = [randint(0, 100) for i in range(100)]
# b = deepcopy(a)
print(merge_sort(a))
# # a = [i for i in range(100)]
# # b = [i for i in range(100)]

# a = [i for i in range(100, -1, -1)]
# b = [i for i in range(100, -1, -1)]

print(a)
# merge_sort(a)
#
# mergetest = timeit.Timer(lambda: merge_sort(a))
# mergeresult = mergetest.repeat(repeat=1000, number=1)
# print(np.amin(mergeresult)*1000, np.amax(mergeresult)*1000, np.median(mergeresult)*1000, np.average(mergeresult)*1000)
print(quick_sort(a))
print(a)
# quicktest = timeit.Timer(lambda: quick_sort(b))
# quickresult = quicktest.repeat(repeat=1000, number=1)
# print(np.amin(quickresult)*1000, np.amax(quickresult)*1000, np.median(quickresult)*1000, np.average(quickresult)*1000)