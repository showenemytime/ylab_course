import random


# В версии 1.1 добавлена проверка для робота. Если ранее робот проигрывал как только соберёт 5 в ряд при рандомном выборе
# то сейчас выбор всё также рандомный, но у компьютера есть право на ошибку. А именно, чтобы компьютер проиграл, нужно
# 5 раз за ход выбрать не правильную клетку из-за которой наступит проигрыш. При том, если пк выбирает клетку, но счётчик
# меньше 5, тогда клетка возращает свою цифру, а пк выбирает другую клетку.

# генерация матрицы поля боя. 10х10
battle_ground = [[i for i in range(1, 11)],
                 [i for i in range(11, 21)],
                 [i for i in range(21, 31)],
                 [i for i in range(31, 41)],
                 [i for i in range(41, 51)],
                 [i for i in range(51, 61)],
                 [i for i in range(61, 71)],
                 [i for i in range(71, 81)],
                 [i for i in range(81, 91)],
                 [i for i in range(91, 101)]]


# функция для отрисовки поля
def draw_ground():
    for i in battle_ground:
        for j in range(10):
            print(f'| {str(i[j]).ljust(3)} ', end='|')
        print()


# ход игрока.
def player_turn():
    while True:
        choice = input('Выберите клетку: ')  # просим ввести число
        if choice.isdigit():
            choice = int(choice)
        else:  # проверяем, что ввели действительно число
            print('--- Введите цифру от 1 до 100 ---')
            continue
        if 101 > choice > 0 and choice:     # проверяем, что число от 1 до 100
            if choice == 100:
                if str(battle_ground[9][9]) in 'XO':    # отдельно ли проверяем занятость ячейки 100
                    print('Эта клетка занята')
                    continue
                else:
                    battle_ground[9][9] = 'X'
                    break

            else:
                if point_is_null(choice):  # проверяем на занятость остальные ячейки
                    print('Эта клетка занята')
                    continue
                else:
                    if choice % 10 == 0:        # ищем клетку, которую указал игрок и ставим в неё свой знак
                        battle_ground[choice // 10 - 1][choice % 10 - 1] = 'X'
                    else:
                        battle_ground[choice // 10][choice % 10 - 1] = 'X'

                    break
        else:
            print('Выберите другую клетку: ')


# логика для хода компьютера
def computer_turn():
     # Счётчик ошибок, если пк ошибётся 5 раз за ход, то проиграет.
    count_computer_error = 0

    while True:

        choice = random.randint(1, 100)  # генерируем число

        if choice == 100:  # сразу проверяем, если число 100, занята ли ячейка, если нет, то занимаем сами
            if str(battle_ground[9][9]) in 'XO':
                continue
            else:
                battle_ground[9][9] = 'O'
                print('COMPUTER choose point: ', choice)
                break

        if point_is_null(choice):  # провека на свободную ячейку
            continue
        else:  # ищем ячейку и ставим свой знак.
            if choice % 10 == 0:
                battle_ground[choice // 10 - 1][choice % 10 - 1] = 'O'
                if is_defeat() and count_computer_error < 5:  # проверка на 5 ошибок пк подряд

                    battle_ground[choice // 10 - 1][choice % 10 - 1] = choice
                    count_computer_error += 1
                    continue
                print('COMPUTER choose point: ', choice)
            else:
                battle_ground[choice // 10][choice % 10 - 1] = 'O'
                print('COMPUTER choose point: ', choice)
                if is_defeat() and count_computer_error < 5:  # проверка на 5 ошибок пк подряд
                    battle_ground[choice // 10][choice % 10 - 1] = choice
                    count_computer_error += 1
                    continue
            break


# проверка на то, что ячейка пустая и можно поставить свой знак.
def point_is_null(choice):
    if choice % 10 == 0:
        choice = battle_ground[choice // 10 - 1][choice % 10 - 1]
    else:
        choice = battle_ground[choice // 10][choice % 10 - 1]
    if str(choice) in 'XO':
        return True
    return False


#  функция со всеми проверками на проигрыш
def is_defeat():
    if gorizont_lose():
        return True
    if vertical_lose():
        return True
    if diagonal_lose_left_right():
        return True
    if diagonal_lose_right_left():
        return True


#  условие проигрыша по горизонтали. Другие проверки работают по аналогичной логике, но с другими диапозонами.
def gorizont_lose():
    for i in range(len(battle_ground)):  # берем все листы
        for j in range(6):  # перём первые 6 из каждого листа. Больше 6 нет смысла, так как остаётся только 4.
            if str(battle_ground[i][j]) in 'XO':  # пробегаюсь по листу и ищу вхождение 'XO'
                sign = battle_ground[i][j]  # нахожу вхождение и запоминаю знак Х или О
                strike = 0                  # добавляю счётчик вхождений подряд
                for k in range(1, 5):

                    if battle_ground[i][j+k] == sign:  # проверяю следующие 4 элемента, после того как нашёл вхождение
                        strike += 1  # плюсую счётчик за каждое найденное вхождение подряд
                        if strike == 4:  # если счётчик 4, значит нашёл 5 одинаковых элементов подряд
                            return True


# проверка на проигрыш по вертикали
def vertical_lose():
    for i in range(6):
        for j in range(len(battle_ground)):
            if str(battle_ground[i][j]) in 'XO':
                sign = battle_ground[i][j]
                strike = 0
                for k in range(1, 5):
                    if battle_ground[i + k][j] == sign:
                        strike += 1
                        if strike == 4:
                            return True


# проверка на проигрыш по диагонали с лева на право
def diagonal_lose_left_right():
     for i in range(6):
         for j in range(6):
             if str(battle_ground[i][j]) in 'XO':
                 sign = battle_ground[i][j]
                 strike = 0

                 for k in range(1, 5):
                     if battle_ground[i + k][j + k] == sign:
                         strike += 1

                         if strike == 4:
                             return True


# проверка на проигрыш по диагонали с права на лево
def diagonal_lose_right_left():
    for i in range(6):
        for j in range(4, 10):
            if str(battle_ground[i][j]) in 'XO':
                sign = battle_ground[i][j]
                strike = 0
                for k in range(1, 5):
                    if battle_ground[i + k][j - k] == sign:
                        strike += 1
                        if strike == 4:
                            return True


# проверка на ничью. Если во всем battle_ground не осталось числа, занчит игра завершена.
def draw():
    for i in range(10):
        if any(str(x) for x in battle_ground[i]):
            return False
    return True


# запускаем основную функцию
def main():

    while True:
        draw_ground()
        player_turn()
        if is_defeat():
            print('Поздравлю, вы проиграли!')
            draw_ground()
            break
        if draw():
            print('Ничья')
            break
        computer_turn()
        if is_defeat():
            print('Поздравлю, вы победили!')
            draw_ground()
            break
        if draw():
            print('Ничья')
            break


# запуск игры
main()
