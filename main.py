import random

q_empty = [['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'],
           ['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
           ['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
           ['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
           ['║', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '║'],
           ['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝']
           ]

q_X = [['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'],
       ['║', ' ', ' ', ' ', '╲', ' ', ' ', ' ', ' ', '╱', ' ', ' ', ' ', '║'],
       ['║', ' ', ' ', ' ', ' ', ' ', '╲', '╱', ' ', ' ', ' ', ' ', ' ', '║'],
       ['║', ' ', ' ', ' ', ' ', '╱', ' ', ' ', '╲', ' ', ' ', ' ', ' ', '║'],
       ['║', ' ', ' ', '╱', ' ', ' ', ' ', ' ', ' ', ' ', '╲', ' ', ' ', '║'],
       ['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝']
       ]
q_O = [['╔', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╗'],
       ['║', ' ', ' ', ' ', '╭', '─', '─', '─', '─', '╮', ' ', ' ', ' ', '║'],
       ['║', ' ', ' ', ' ', '│', ' ', ' ', ' ', ' ', '│', ' ', ' ', ' ', '║'],
       ['║', ' ', ' ', ' ', '│', ' ', ' ', ' ', ' ', '│', ' ', ' ', ' ', '║'],
       ['║', ' ', ' ', ' ', '╰', '─', '─', '─', '─', '╯', ' ', ' ', ' ', '║'],
       ['╚', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '═', '╝']
       ]

m = [['', '', ''], ['', '', ''], ['', '', '']]


# забиваю матрицу случайными значениями(для тестов делал)
def randomizmatrix():
    for k in range(3):
        for i in range(3):
            m[k][i] = random.choice(['0', 'O', 'X'])


# забиваю матрицу пустотой
def fillmatrix():
    for k in range(3):
        for i in range(3):
            m[k][i] = '0'


# проверка на выигрыш
def victory_checker(x, y, symb):
    ch1 = [symb, symb, symb] in m  # ряды
    ch2 = [symb, symb, symb] in list(map(list, zip(*m[::-1])))  # повернул матрицу на 90
    ch3 = m[0][0] == m[1][1] == m[2][2] != '0'  # диагональ
    ch4 = m[0][2] == m[1][1] == m[2][0] != '0'  # диагональ

    if any([ch1, ch2, ch3, ch4]):
        return True
    else:
        return False

# Вывод псевдографиики из игровой матрицы 3*3 на экран из словаря с матрицами графических представлений
def MatrixScreenOutput():
    matrx = {'X': q_X, 'O': q_O, '0': q_empty}

    for i in range(3):
        for y in range(6):
            Lin = list(matrx[m[i][0]][y] + matrx[m[i][1]][y] + matrx[m[i][2]][y])
            l = ''
            for a in Lin:
                l += a
            print(l)


def coord_input():
    while True:
        coord = input('Введите координаты в формате строка(1-3) столбец(1-3)  ')
        coord = (coord.replace(' ', ''))
        if coord in ['11', '12', '13', '21', '22', '23', '31', '32', '33']:
            X = int(coord[0])
            Y = int(coord[1])
            break
        print("--------------Ошиблись при вводе, будьте внимательны!-----------")
    return (X - 1, Y - 1)

player_name = {0: "КРЕСТИКИ", 1: "НОЛИКИ"}
sign = {0: "X", 1: "O"}
trigger = 0
fillmatrix()
MatrixScreenOutput()

draw = True
for mov_count in range(9):
    while True:
        print("Делают ход", player_name[trigger])
        coord = coord_input()
        Xc = coord[0]
        Yc = coord[1]
        if m[Xc][Yc] == '0':
            m[Xc][Yc] = sign[trigger]
            break
        print("Клетка уже занята, ")

    MatrixScreenOutput()

    if victory_checker(Xc, Yc, sign[trigger]):
        print(player_name[trigger], "победили!")
        draw = False
        break
    trigger = 1 - trigger

if draw:
    print("Ничья! попробуйте ещ раз")
