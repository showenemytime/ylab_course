import math


# фукнция вычисления колчиства нулей в конце факториала
def zeros(n):
    factorial = str(math.factorial(n))[::-1]  # получаем факториал числа, преобразуем в строку и переворачиваем
    count = 0  # создаём счётчик
    for digit in factorial:  # проходимся по каждому числу в строке.
        if digit == '0':  # если число == 0, тогда увеличиваем счётчик на 1
            count += 1
        else:  # иначе завершаем цикл
            break

    return count


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(12) == 2

print('All tests passed!')
