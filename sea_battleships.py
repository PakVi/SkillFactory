from random import randint
# from random import randrange
# from random import choice
# import random



# pole = [[" " for _ in range(0, 6)] for _ in range(0, 6)]
#
# ship = [[0, 0], [0, 1], [0, 2], [0, 3]]
# palubi = 4
#
# def random_ship():
#   global ship
#   x = random.randint(0, 4)
#   y = random.randint(0, 4)
#   d = random.randint(0, 1)
#   if d == 0:
#     ship = [[x, y], [x, y+1], [x, y+2], [x, y+3]]
#   else:
#     ship = [[x, y], [x+1, y], [x+2, y], [x+3, y]]
#
#
# def show_pole():
#   for row in pole:
#     print('|'.join(row))
#     print('-'*15)
#
# def kuda_strelat():
#   global palubi      #---
#   print('Укажите столбец:')
#   stolbec = int(input())
#   print('Укажите ряд:')
#   ryad = int(input())
#
#   if [ryad, stolbec] in ship:
#     if pole[ryad][stolbec] != '#':   #----
#       print('Попал!')
#       pole[ryad][stolbec] = '#'
#       palubi = palubi - 1
#       if palubi == 0:
#         print('Вы победили!!')
#   else:
#     print('Мимо...')
#     pole[ryad][stolbec] = '~'
#
#
# show_pole()
# random_ship()
# for i in range(10):
#   kuda_strelat()
#   show_pole()
# pole = [["o" for _ in range(0, 6)] for _ in range(0, 6)]
#
#
# def poles():
#     print("  1 2 3 4 5 6")
#     for row in range(len(pole)):
#         print(row + 1, *pole[row])
#
#
# print(poles())
# print(len(pole))
# x1 = randint(0, len(pole) - 1)
# y1 = randint(0, len(pole) - 1)
# print(x1, y1)
#
# pole[x1][y1] = "▀"
#
# print(poles())
# h = randint(0, 1)




# class Box: # класс стостояния ячеек
#
#     def set_objects(text):
#         return text
#
#     ship_box = set_objects("■")
#     empty_box = set_objects("o")
#     miss_box = set_objects("*")
#     damage_box = set_objects("□")
#     kill_box = set_objects("X")

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other): # проверка на равенство точек
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Out of range"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Уже сюда стреляли"


class BoardWrongShipException(BoardException):
    pass


# class Ship: # класс корабля,. его размер точки начала корабля, ориентация
#     def __init__(self, size, x, y, direction):
#         self.size = size
#         self.health = size
#         self.x = x
#         self.y = y
#         self.direction = direction
#         self.set_direction(direction)
#
#     def __init__(self):
#         return Box.ship_box
#
#     def set_position(self,x, y, d):
#         self.x = x
#         self.y = y
#         self.set_direction(d)
#    def check_ship(self, ship, element):
#
#         field = self.get_field(element)
#
#         if ship.x + ship.horizontal - 1 >= self.size or ship.x < 0 or \
#                 ship.y + ship.vertikal - 1 >= self.size or ship.y < 0:
#             return False
#
#         x = ship.x
#         y = ship.y
#         horizontal = ship.horizontal
#         vertikal = ship.vertikal
#
#         for p_x in range(x, x + vertikal):
#             for p_y in range(y, y + horizontal:
#                 if str(field[p_x][p_y]) == Cell.miss_cell:
#                     return False
#
#         for p_x in range(x - 1, x + vertikal + 1):
#             for p_y in range(y - 1, y + horizontal + 1):
#                 if p_x < 0 or p_x >= len(field) or p_y < 0 or p_y >= len(field):
#                     continue
#                 if str(field[p_x][p_y]) in (Cell.ship_cell, Cell.destroyed_ship):
#                     return False
#
#         return True
#
#     def set_direction(self, d):
#
#         self.direction = d
#
#         if self.direction == 0:
#             self.vertikal = self.size
#             self.horizontal = 1
#         elif self.direction == 1:
#             self.vertikal = 1
#             self.horizontal = self.size
#
# class FieldSort(object):
#     main="poles"
#     other = "other"
#
#
#
# class Field:
#     def __init__(self size):
#         self.size = size
#
#
#         self.poles = [[Box.empty_box for _ in range(size)] for _ in range(size)]
#
#     def get_field(self, element):
#         if element == FieldSort.main:
#             return self.poles
#
#
#
#     def __str__(self):
#         lines = ""
#         lines += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
#         for i, row in enumerate(self.poles):
#             lines += f"\n{i + 1} | " + " | ".join(row) + " |"
#
#         return lines
#
#      def add_ship(self, ship, element):
#
#          field = self.get_field(element)
#
#           #x = ship.x
#           #y = ship.y
#           vertikal = ship.vertikal
#           horizontal = ship.horizontal
#           x = randint(0, 5)
#           y = randint(0, 5)
#           field[x][y] == Box.ship_box
#
#           for p_x in range (x, x+ horizontal):
#               for p_y in range (y, y+vertikal):
#               self.pole[p_x][p_y] = ship



class Ship:

    def __init__(self, nouse, lenght, rotation): # точка носа корабля, длянна, направление.
        self.nouse=nouse
        self.lenght=lenght
        self.rotation=rotation
        self.hp=lenght

    @property #
    def dots(self):
        ship_dots = [] # точки занятые короблем
        for i in range(self.lenght):
            x1= self.nouse.x
            y1= self.nouse.y

            if self.rotation == 0: # направление корабля
                x1+= i

            elif self.rotation == 1:
                y1+= i

            ship_dots.append(Dot(x1, y1))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False, size=6):
        self.size= size
        self.hid= hid

        self.count= 0

        self.field= [["o"] * size for _ in range(size)]

        self.busy= []
        self.ships= []

    def contour(self, ship, verb=False):
        near= [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)] # смещения от точки занятой кораблем и последуещее изменение ячеки
        for d in ship.dots:
            for dx, dy in near:
                cur= Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y]= "."
                    self.busy.append(cur)
    def add_ship(self, ship):

        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y]= "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def __str__(self):
        lines= ""
        lines+= "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            lines+= f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            lines= lines.replace("■", "o")
        return lines

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships: # проверка, есть ли точка в списке точек, занятых кораблями
            if d in ship.dots:
                ship.hp-= 1
                self.field[d.x][d.y]= "X"
                if ship.hp== 0:
                    self.count+= 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен")
                    return False
                else:
                    print("Корабль подбит")
                    return True

        self.field[d.x][d.y]= "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy= []


class Player:
    def __init__(self, board, enemy):
        self.board= board
        self.enemy= enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target= self.ask() # попытка сделать выстрел
                repeat= self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d= Dot(randint(0, 5), randint(0, 5)) # рандомный выбор 2 точек
        print(f"Ход противника {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords= input("Ваш ход ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты ")
                continue

            x, y= cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y= int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    def __init__(self, size=6):
        self.size= size
        player= self.random_board() #генерация досок
        computer= self.random_board()
        computer.hid= True # для компьютера идет скрытие кораблей, замена кораблей о

        self.ai= AI(computer, player)
        self.us= User(player, computer)

    def random_board(self):
        board= None
        while board is None:
            board= self.random_place()
        return board

    def random_place(self):
        lens= [3, 2, 2, 1, 1, 1] # список кораблей
        board= Board(size=self.size)
        attempts= 0 # кол-во попыток поставить корабль
        for l in lens:
            while True:
                attempts+= 1
                if attempts > 2000:
                    return None
                ship= Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board




    def loop(self): # игровой цикл
        num = 0 #считает номер хода
        while True:
            print("Ваше поле")
            print(self.us.board)
            print("Поле противника")
            print(self.ai.board)
            if num % 2== 0: #четный ход-ход игрока
                print("Ваш ход. ввседите номер строки и столбца")
                repeat= self.us.move() #
            else:
                print("Ход противника")
                repeat= self.ai.move()
            if repeat:
                num-= 1

            if self.ai.board.count== 6:
                print("Победа")
                break

            if self.us.board.count== 6:
                print("Противник выиграл")
                break
            num+= 1

    def start(self):
        self.loop()


g = Game()
g.start()