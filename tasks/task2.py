class FirstCircBuf:
    """Класс кольцевой буфер.
    Плюсы: простота и читабельность
    Недостатки: при закольцовывании буфера
    значения индексов(переменные tail_index и head_index)
    следуют друг за другом, ссылаясь на одно и то же значение,
    следовательно можно избавиться от одного из них

    >>> buffer = FirstCircBuf(4)
    >>> buffer.enqueue(1)
    >>> buffer.enqueue(2)
    >>> buffer.enqueue(3)
    >>> buffer.enqueue(4)
    >>> buffer.enqueue(5)
    >>> buffer.enqueue(6)
    >>> buffer.enqueue(7)
    >>> buffer.enqueue(8)
    >>> buffer.dequeue(3)
    [5, 6, 7]
    """
    def __init__(self, capacity: int):
        self.buffer: list = []
        self.capacity = capacity
        self.head_index = self.tail_index = 0

    def enqueue(self, num: int):

        if self.tail_index >= self.capacity:
            self.buffer[self.tail_index % self.capacity] = num

        elif self.tail_index < self.capacity:
            self.buffer.append(num)

        self.tail_index += 1

        if len(self.buffer) == self.capacity:
            self.head_index = self.tail_index % self.capacity

    def dequeue(self, size_to_read: int):
        if size_to_read > len(self.buffer):
            return None

        result_to_read = []

        index = self.head_index
        while size_to_read > 0 and index < len(self.buffer):
            result_to_read.append(self.buffer[index])
            index += 1
            size_to_read -= 1
        index = 0

        while index < size_to_read:
            result_to_read.append(self.buffer[index])
            index += 1
        return result_to_read


class SecondCircBuf:
    """Класс кольцевой буфер.
    Плюсы: не включает в себя избыточного числа переменных
    Минусы: Явное лучше неявного

    >>> buffer = SecondCircBuf(4)
    >>> buffer.enqueue(1)
    >>> buffer.enqueue(2)
    >>> buffer.enqueue(3)
    >>> buffer.enqueue(4)
    >>> buffer.enqueue(5)
    >>> buffer.enqueue(6)
    >>> buffer.enqueue(7)
    >>> buffer.enqueue(8)
    >>> buffer.dequeue(3)
    [5, 6, 7]
    """
    def __init__(self, capacity: int):
        self.buffer: list = []
        self.capacity = capacity
        self.tail_index = 0

    def enqueue(self, num: int):

        if self.tail_index >= self.capacity:
            self.buffer[self.tail_index % self.capacity] = num

        elif self.tail_index < self.capacity:
            self.buffer.append(num)

        self.tail_index += 1

    def dequeue(self, size: int):
        if size > len(self.buffer):
            return None

        result_to_read = []

        if len(self.buffer) < self.capacity:
            for value in self.buffer:
                result_to_read.append(value)
            return result_to_read

        index = self.tail_index % self.capacity
        while size > 0 and index < len(self.buffer):
            result_to_read.append(self.buffer[index])
            index += 1
            size -= 1

        index = 0
        while index < size:
            result_to_read.append(self.buffer[index])
            index += 1

        return result_to_read


if __name__ == '__main__':
    import doctest
    doctest.testmod()
