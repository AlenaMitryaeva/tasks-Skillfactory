playfield = [[" _"]*3 for i in range(3)]

def playmap():
    print((f"   0 1 2").ljust(6))
    for i in range(3):
        print(f"{i}{playfield[i][0]} {playfield[i][1]} {playfield[i][2]}")

win1 = [(0, 0), (0, 1), (0, 2)]
win2 = [(1, 0), (1, 1), (1, 2)]
win3 = [(2, 0), (2, 1), (2, 2)]
win4 = [(0, 2), (1, 1), (2, 0)]
win5 = [(0, 0), (1, 1), (2, 2)]
win6 = [(0, 0), (1, 0), (2, 0)]
win7 = [(0, 1), (1, 1), (2, 1)]
win8 = [(0, 2), (1, 2), (2, 2)]
win = [win1, win2, win3, win4, win5, win6, win7, win8]

def winner(j):
    for i in win:
        i1 = set(i)
        m = j.intersection(i1)
        if m == i1:
            return True

    return False

print("Игра крестики и нолики", "Ввод X = строка, Y = столбец", "Вводить можно только числа!", "Начинают крестики!",
          sep = "\n")
playmap()

counter = 1
c = []
d = []

while True:
    x = input("Введите координату Х")
    y = input("Введите координату Y")
    if not (x.isdigit()) or not (y.isdigit()):
        print("Это не числа! ")
        continue
    move = int(x)
    move2 = int(y)
    if not 0 <= move <=2 or not 0 <= move2 <=2:
        print("Координаты вне допустимых границ")
        continue
    if counter <9:
        if counter%2 ==1:
            if playfield[move][move2] == " _":
               playfield[move][move2] = " X"
               playmap()
               counter += 1
               c += [(move,move2)]
               c1 = set(c)
               winner(c1)
               if winner(c1):
                   print ("Победили крестики!")
                   break
            else:
                print("Клетка занята")
                continue
        else:
            if playfield[move][move2] == " _":
                playfield[move][move2] = " 0"
                playmap()
                counter += 1
                d += [(move,move2)]
                d1 = set(d)
                winner(d1)
                if winner(d1):
                    print("Победили нолики!")
                    break
            else:
                print("Клетка занята")
                continue
    else:
        if playfield[move][move2] == " ":
           playfield[move][move2] = " X"
           playmap()
           c += [(move, move2)]
           c1 = set(c)
           winner(c1)
           if winner(c1):
               print("Победили крестики!")
               break
           else:
               print("Ничья! Игра окончена!")
               break
        else:
           print("Клетка занята")
        continue




