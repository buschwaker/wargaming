import unittest
from tasks import task3, task1, task2


class TestSorts(unittest.TestCase):
    """Тестируем сортировки."""

    def setUp(self):
        self.random_list = [4, 1, 2, 5, 8, 1]
        self.sorted_asc = [1, 2, 3, 4, 5, 6]
        self.sorted_desc = [6, 5, 4, 3, 2, 1]

        self.result_random_list = [1, 1, 2, 4, 5, 8]
        self.result_sorted_asc = [1, 2, 3, 4, 5, 6]
        self.result_sorted_desc = [1, 2, 3, 4, 5, 6]

    def test_quick_sort(self):
        """Тестируем быструю сортировку"""
        call_random = task3.quick_sort(self.random_list)
        call_sorted_asc = task3.quick_sort(self.sorted_asc)
        call_sorted_desc = task3.quick_sort(self.sorted_desc)

        self.assertEqual(
            call_random, self.result_random_list,
            'Функция quick_sort() не работает со списком случайных значений'
        )
        self.assertEqual(
            call_sorted_asc, self.result_sorted_asc,
            'Функция quick_sort() не работает с сортированным списком'
        )
        self.assertEqual(
            call_sorted_desc, self.result_sorted_desc,
            'Функция quick_sort() не работает со '
            'списком случайных значений(от большего к меньшему)'
        )

    def test_merge_sort(self):
        """Тестируем сортировку слиянием"""
        call_random = task3.merge_sort(self.random_list)
        call_sorted_asc = task3.merge_sort(self.sorted_asc)
        call_sorted_desc = task3.merge_sort(self.sorted_desc)

        self.assertEqual(
            call_random, self.result_random_list,
            'Функция merge_sort() не работает со списком случайных значений'
        )
        self.assertEqual(
            call_sorted_asc, self.result_sorted_asc,
            'Функция merge_sort() не работает с сортированным списком'
        )
        self.assertEqual(
            call_sorted_desc, self.result_sorted_desc,
            'Функция merge_sort() не работает со '
            'списком случайных значений(от большего к меньшему)'
        )


class TestIfEven(unittest.TestCase):
    """Тестируем алгоритмы определения четности числа."""

    @classmethod
    def setUp(cls):
        cls.data = {
            task1.if_even_plain:
                ((0, True), (8, True), (5, False), (-10, True)),
            task1.if_even_recursive:
                ((0, True), (8, True), (5, False), (-10, True)),
            task1.if_even_one_intersection:
                ((0, True), (8, True), (5, False), (-10, True)),
        }

    def test_if_plain_even(self):
        """Тестируем все 3 функции определения четности числа"""
        for func, numbers_and_if_even in TestIfEven.data.items():
            with self.subTest(func=func):
                for number in numbers_and_if_even:
                    with self.subTest(number=number):
                        self.assertEqual(func(
                            number[0]),
                            number[1],
                            f'Функция {func.__name__} не '
                            f'возвращает {number[1]} для {number[0]}'
                        )


class CircularBuffer(unittest.TestCase):
    """Тестируем циклические буферы."""

    @classmethod
    def setUp(cls):
        cls.buffer_classes = (task2.FirstCircBuf, task2.SecondCircBuf)

    def test_buffer_class(self):
        """Тестируем считывание 3 элементов из буфера с 4 элементами"""
        for Class_Buf in CircularBuffer.buffer_classes:
            with self.subTest(Class_Buf=Class_Buf):
                buffer = Class_Buf(4)
                for i in range(1, 9):
                    buffer.enqueue(i)
                self.assertEqual(buffer.dequeue(3), [5, 6, 7])

    def test_read_more_than_capacity(self):
        """Тестируем считывание 5 элементов из буфера с 4 элементами"""
        for Class_Buf in CircularBuffer.buffer_classes:
            with self.subTest(Class_Buf=Class_Buf):
                buffer = Class_Buf(4)
                for i in range(1, 9):
                    buffer.enqueue(i)
                self.assertEqual(buffer.dequeue(5), None)


if __name__ == '__main__':
    unittest.main()
