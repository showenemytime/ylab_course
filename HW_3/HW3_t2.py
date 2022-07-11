import time
from typing import Callable

'''  
  Функция декоратор, повторяет основную функцию определенное количество раз с задержкой, которая также растёт
  call_count - Счётчик повторений
  start_sleep_time - Начальное время задержки выполнения фунции
  factor - Множитель, который участвует в расчёте экспоненциального роста зажержки
  border_sleep_time - Граница, дальше которой не уйдёт задержка
'''


def repeat_func(func) -> Callable[[int, int, int, int], None]:

    def wrapper(call_count=4, start_sleep_time=1, factor=2, border_sleep_time=15) -> None:
        print(f'Количество запусков: {call_count}')
        print(f'Начало работы.\n')
        call_count_counter: int = 1  # Счётчик повторений цикла.

        #  Цикл, в котором увеличиваем задержку по формуле.
        while start_sleep_time <= border_sleep_time and call_count >= call_count_counter:
            time.sleep(start_sleep_time)

            # Условия для выбора окончания в слове "секудна".
            if start_sleep_time == 1:
                sec: str = 'секунда'
            elif start_sleep_time in (2, 3, 4):
                sec: str = 'секунды'
            else:
                sec: str = 'секунд'

            print(f'Запуск номер {call_count_counter}. Ожидание: {start_sleep_time} {sec}. Результат = {func()}')
            call_count_counter += 1
            if start_sleep_time < border_sleep_time:
                start_sleep_time = start_sleep_time * 2 ** factor
            if start_sleep_time > border_sleep_time:
                start_sleep_time = border_sleep_time
        return None
    return wrapper


@repeat_func
def func_result() -> str:
    txt: str = 'Я внешняя функция и до сих пор работаю'
    return txt


if __name__ == '__main__':
    func_result()
