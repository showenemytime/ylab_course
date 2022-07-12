import time
from typing import Callable, Any

'''  
  Функция декоратор, повторяет основную функцию определенное количество раз с задержкой, которая также растёт
  call_count - Счётчик повторений
  start_sleep_time - Начальное время задержки выполнения фунции
  factor - Множитель, который участвует в расчёте экспоненциального роста зажержки
  border_sleep_time - Граница, дальше которой не уйдёт задержка
'''


def repeat_func(call_count=3, start_sleep_time=1, factor=2, border_sleep_time=15) -> \
        Callable[[Any], Callable[[], None]]:
    t = start_sleep_time

    def decorator(func):
        def wrapper() -> None:
            sleep_time: int = t
            print(f'Количество запусков: {call_count}')
            print(f'Начало работы.\n')
            call_count_counter: int = 1  # Счётчик повторений цикла.

            #  Цикл, в котором увеличиваем задержку по формуле.
            while sleep_time <= border_sleep_time and call_count >= call_count_counter:
                time.sleep(sleep_time)

                # Условия для выбора окончания в слове "секудна".
                if sleep_time == 1:
                    sec: str = 'секунда'
                elif sleep_time in (2, 3, 4):
                    sec: str = 'секунды'
                else:
                    sec: str = 'секунд'

                print(f'Запуск номер {call_count_counter}. Ожидание: {sleep_time} {sec}. Результат = {func()}')
                call_count_counter += 1
                if sleep_time < border_sleep_time:
                    sleep_time = sleep_time * 2 ** factor
                if sleep_time > border_sleep_time:
                    sleep_time = border_sleep_time
            return None

        return wrapper

    return decorator


@repeat_func(call_count=4)
def func_result() -> str:
    txt: str = 'Я внешняя функция и до сих пор работаю.'
    return txt


if __name__ == '__main__':
    func_result()
