# Проверка, было ли ранее вычисление с конкретным числом, если да, то берём ответ из cache_dict, иначе вычисляем
def cache(func) -> any:
    cache_dict = {}

    # проверяем, есть ли в словаре значение, если нет, то вычисляем и добавляем в словарь ключ и значение
    def wrapper(num: int):
        result = func(num)
        if num in cache_dict:
            print(f'Достал из кэша ответ {cache_dict[num]}')

            return cache_dict[num]
        else:
            print(f'Ответ {result}, добавил его в кэш')
            cache_dict[num] = result
            return result

    return wrapper


@cache
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    for i in [1, 1, 3, 4, 4]:  # для проверки работы кэша
        multiplier(i)
