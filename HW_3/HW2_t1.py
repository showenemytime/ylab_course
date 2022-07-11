class CyclicIterator:
    def __init__(self, obj):  # Инициирую класс, чтобы принимать объект.
        self.obj = obj
        self.iter = iter(self.obj)

    def __iter__(self):  # Обьявляю класс итерируемым.
        return self

    def __next__(self):  # Описываю логику работы.
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.obj)
            return next(self.iter)


if __name__ == "__main__":
    cyclic_iterator = CyclicIterator(range(3))
    [print(i) for i in cyclic_iterator]
