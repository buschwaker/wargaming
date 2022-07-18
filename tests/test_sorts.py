import unittest
from tasks import task3


class TestSorts(unittest.TestCase):
    """Тестируем quick_sort."""

    def setUp(self):
        self.random_list = [4, 1, 2, 5, 8, 1]
        self.sorted_asc = [1, 2, 3, 4, 5, 6]
        self.sorted_desc = [6, 5, 4, 3, 2, 1]

        self.result_random_list = [1, 1, 2, 4, 5, 8]
        self.result_sorted_asc = [1, 2, 3, 4, 5, 6]
        self.result_sorted_desc = [1, 2, 3, 4, 5, 6]

    def test_quick_sort(self):
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


if __name__ == '__main__':
    unittest.main()
