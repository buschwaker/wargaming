# =============================================================================
# № 1 c tail и head
# Есть два несвязанных друг с другом индекса (в реализации с/с++ это были бы указатели), каждый из
# которых имеет свое назначение, а именно:
# head всегда указывает на ячейку, начиная с которой требуется считывает данные из буфера;
# tail всегда указывает на ячейку, начиная с которой требуется записывать данные в буфер.
# Преимущество: каждая переменная играет свою конкретную роль, легко разобраться в коде.
# Недостаток: при написании кода мне показалось, что количество переменных избыточно, так как
# после первого полного заполнении буфера при дальнейшем затирании старых значений tail и head всегда двигаются вместе и рядом.
# Что логично, так как структура данных закольцована. В виду этого можно было бы избавиться от одной из них,
# оставив лишь tail, что и показано в примере №2.
# =============================================================================

class CircularBuffer:
    def __init__(self, size):
        self.capacity = size
        self.data = []
        self.head_index = 0
        self.tail_index = 0

    def write(self, value):

        if (self.tail_index < self.capacity):
            self.data.append(value)

        elif (self.tail_index >= self.capacity):
            self.data[self.tail_index % self.capacity] = value

        self.tail_index += 1

        if (len(self.data) == self.capacity):
            self.head_index = self.tail_index % self.capacity

    def read(self, size):
        if (size > len(self.data)):
            return

        data = []

        index = self.head_index
        while (size > 0 and index < len(self.data)):
            data.append(self.data[index])
            index += 1
            size -= 1
        index = 0

        while (index < size):
            data.append(self.data[index])
            index += 1

        return data


# =============================================================================
# № 2 c tail
# Есть теперь лишь tail, который всегда указывает на ячейку, начиная с которой требуется записывать данные в буфер.
# Преимущество: отсутсиве изботочного числа переменных.
# Недостаток: труднее разобраться в коде.
# =============================================================================

class CircularBuffer:
    def __init__(self, size):
        self.capacity = size
        self.data = []
        self.tail_index = 0

    def write(self, value):

        if (self.tail_index < self.capacity):
            self.data.append(value)

        elif (self.tail_index >= self.capacity):
            self.data[self.tail_index % self.capacity] = value

        self.tail_index += 1

    def read(self, size):
        if (size > len(self.data)):
            return

        data = []

        if (len(self.data) < self.capacity):
            for value in self.data:
                data.append(value)
            return data

        index = self.tail_index % self.capacity
        while (size > 0 and index < len(self.data)):
            data.append(self.data[index])
            index += 1
            size -= 1

        index = 0
        while (index < size):
            data.append(self.data[index])
            index += 1

        return data


buffer = CircularBuffer(4)
buffer.write(1)
buffer.write(2)
print(buffer.read(2))

buffer.write(3)
buffer.write(4)
buffer.write(5)
buffer.write(6)
buffer.write(7)
print(buffer.read(4))
buffer.write(8)
buffer.write(9)
print(buffer.read(3))


# =============================================================================
# № 3 этот пример по сути идентичен предыдущему. Однако, при помощи классов
# четко отделены два случая взаимодействия с буффером: 1. когда он еще не замкнулся 2. уже замкнулся.
# Не стала реализовывать здесь функцию чтения куска буфера заданного размера, чтобы не отягощать пример.
# Преимущество: при такой реализации проще разобраться в логике.
# Недостаток: архитектура решения вышла более грамоздкой и менее производительной.
# =============================================================================

class CircularBuffer:
    def __init__(self, size):
        self.capacity = size
        self.data = []

    def write(self, value):
        self.data.append(value)

        if (len(self.data) == self.capacity):
            self.count = 0
            self.__class__ = self.__Full

    def readAll(self):
        return self.data

    class __Full:

        def write(self, value):
            self.data[self.count] = value
            self.count = (self.count + 1) % self.capacity

        def readAll(self):
            return self.data[self.count:] + self.data[: self.count]


buffer = CircularBuffer(2)
buffer.write(1)
buffer.write(2)
buffer.write(3)
buffer.write(4)
buffer.write(5)
buffer.write(6)
buffer.write(7)
print(buffer.readAll())

buffer.write(8)
buffer.write(9)

print(buffer.readAll())