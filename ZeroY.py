from random import randint

winGo = [(1,2,3),
         (4,5,6),
         (7,8,9),
         (1,4,7),
         (2,5,8),
         (3,6,9),
         (1,5,9),
         (3,5,7)]

def instruct():
    print(
"""Добро пожаловать на интелектуальную игру 'Крестики-нолики' """)
instruct()

def Pieces():
    cell = [i for i in range(1,10)]
    return cell

def Display(net_list):
    print('+---+---+---+')
    for i in range(0,len(net_list)):
        if net_list[i] in range(1,10):
            print(f'| \033[46m{net_list[i]} \033[0m', end='')
        elif net_list[i] == 'X' :
            print(f'| \033[33m{net_list[i]} \033[0m', end='')
        elif net_list[i] == 'O':
            print(f'| \033[41m{net_list[i]} \033[0m', end='')
        if i==2 or i == 5 or i==8:
            print (f'|\n+---+---+---+')

def Boards(index, net, symbol):
    net[index-1] = symbol
    # DrawNet(net)

def Winner(winGo, net):
    x_list = LegalMoves(net, 'X')
    o_list = LegalMoves(net, 'O')
    Display(net)
    for i in range(len(winGo)):
        if len(set(x_list).intersection(set(winGo[i]))) == 3:
            print('\033[43mТы выиграл :( \033[0m')
            return False
        elif len(set(o_list).intersection(set(winGo[i]))) == 3:
            print('\033[41mCOMPUTER WIN!\033[0m')
            return False
        elif len(x_list)+len(o_list) == 9:
            print ('Похоже ничья')
            return False

def NextTurn(net):
    empty_list = list(filter(lambda x: type(x) is int, net))
    return empty_list

def LegalMoves(net, symbol):
    player_cells = []
    for i in range(len(net)):
        if net[i] == symbol:
            player_cells.append(i+1)  
    return player_cells

def ComputerMove(net, winGo: set):
    human = LegalMoves(net, 'X')
    bot = LegalMoves(net, 'O')
    empty_cells = NextTurn(net)
    if len(human) >= 2:
        step = Checks(bot, winGo, empty_cells)
        if step != None:
            Boards(step, net, 'O')
            return
        else:
            step = Checks(human, winGo, empty_cells)
            if step != None:
                Boards(step, net, 'O')
                return
    index = randint(0, len(empty_cells)-1)
    step = empty_cells[index]
    Boards(step, net, 'O')
    return

def Checks(players, winGo, empty_list):
    step = None
    for k in range(len(winGo)):
        if len(set(winGo[k]).intersection(set(players))) == 2: 
            step = set(winGo[k]).difference(set(players)).pop()
            if step in empty_list:
                return step
            step = None
    return step

cell = Pieces()
Display(cell)
while True:
    isEmpty = False
    while not isEmpty:
        x = input(f'Твой ход человек -> X // Введи номер ячейки ')
        if x.isdigit(): 
            if int(x) > 0 and int(x) < 10:
                x = int(x)
                isEmpty = True
        Display(cell)
    Boards(x, cell, 'X')   

    if Winner(winGo, cell) == False:
        break
    else: 
        ComputerMove(cell, winGo)
        if Winner(winGo, cell) == False:
            break