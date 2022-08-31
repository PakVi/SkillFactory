pole = [["-" for i in range(0, 3)] for j in range(0, 3)]  # создание списка поле


def poles():  # отрисовка поля
    print("  1 2 3")
    for row in range(len(pole)):
        print(row + 1, *pole[row])


count = 1  # счетчик хода для 2-х игроков
win = 0  # чек победы
count_all = 0  # общее количество ходов


def inputs_x():  # ввод для х
    print("Ход", count)
    print("Ход Х-са")
    x = int(input("Введите номер строки"))
    y = int(input("Введите номер столбца"))

    if 0 < x <= 3 and 0 < y <= 3:  # проверка выхода из зоны координат и занятость ячейки
        if pole[x - 1][y - 1] != "-":
            print("Занято, введите заново")
            inputs_x()
        else:
            pole[x - 1][y - 1] = "x"
            poles()
    else:
        print("Вне координат, Введите заново")
        inputs_x()


def inputs_0():  # ввод для 0
    print("Ход 0-ля")
    x = int(input("Введите номер строки"))
    y = int(input("Введите номер столбца"))

    if 0 < x <= 3 and 0 < y <= 3:
        if pole[x - 1][y - 1] != "-":
            print("Занято, введите заново")
            inputs_0()
        else:
            pole[x - 1][y - 1] = "0"
            poles()
    else:
        print("Вне координат, Введите заново")
        inputs_0()


def check_win():  # проверка победы.
    global win
    if pole[0][0] == pole[0][1] == pole[0][2] == "x" or pole[1][0] == pole[1][1] == pole[1][2] == "x" or pole[2][0] == \
            pole[2][1] == pole[2][2] == "x" or pole[0][0] == pole[1][0] == pole[2][0] == "x" or pole[0][1] == pole[1][
        1] == pole[2][1] == "x" or pole[0][2] == pole[1][2] == pole[2][2] == "x" or pole[0][0] == pole[1][1] == pole[2][
        2] == "x" or pole[0][2] == pole[1][1] == pole[2][0] == "x":
        win += 1
        print("Игрок X Win")

    elif pole[0][0] == pole[0][1] == pole[0][2] == "0" or pole[1][0] == pole[1][1] == pole[1][2] == "0" or pole[2][0] == \
            pole[2][1] == pole[2][2] == "0" or pole[0][0] == pole[1][0] == pole[2][0] == "0" or pole[0][1] == pole[1][
        1] == pole[2][1] == "0" or pole[0][2] == pole[1][2] == pole[2][2] == "0" or pole[0][0] == pole[1][1] == pole[2][
        2] == "0" or pole[0][2] == pole[1][1] == pole[2][0] == "0":
        win += 1
        print("Игрок 0 Win")


def tie():  # проверка на ничью
    global win
    global count_all
    if count_all > 9:
        win += 1
        print("Ничья")

poles()

for i in range(9):
    tie()
    if win > 0:
        break
    count_all += 1
    print("Всего ходов",count_all)
    inputs_x()
    check_win()
    tie()
    if win > 0:
        break
    count_all += 1
    print("Всего ходов",count_all)
    tie()
    if win > 0:
        break
    inputs_0()
    check_win()
    if win > 0:
        break
    count += 1

print(input("Enter - закрыть программу"))
