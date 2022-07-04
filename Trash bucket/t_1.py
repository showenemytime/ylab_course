class CyclicIterator:
    def __init__(self, obj):  # инициирую класс, чтобы принимать объект
        self.obj = obj
        self.iter = iter(self.obj)

    def __iter__(self):  # обьявляю класс итерируемым
        return self

    def __next__(self):  # описываю логику работы
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.obj)
            return next(self.iter)


cyclic_iterator = CyclicIterator(range(3))

[print(i) for i in cyclic_iterator]
