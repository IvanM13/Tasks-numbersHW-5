from random import randint


def GetInput(name):
    n = int(input(f"{name}, Какое количество конфет вы берете (1...28): "))
    while n < 1 or n > 28:
        n = int(input(f"{name}, введите корректное количество конфет: "))
    return n


def GetPrint(name, j, meter, candy):
    print(f"Ходил {name}, он взял {j}, теперь  y него {meter}. Осталось на столе {candy} конфет.")


onePlayer = input("Введите имя первого игрока: ")
twoPlayer = input("Введите имя второго игрока: ")
candy = int(input("Введите количество конфет на столе: "))
winner = randint(0, 2) 
if winner:
    print(f"Первый ходит {onePlayer}")
else:
    print(f"Первый ходит {twoPlayer}")

countOne = 0
countTwo = 0

while candy > 28:
    if winner:
        j =  GetInput(onePlayer)
        countOne += j
        candy -= j
        winner = False
        GetPrint(onePlayer, j, countOne, candy)
    else:
        j = GetInput(twoPlayer)
        countTwo += j
        candy -= j
        winner = True
        GetPrint(twoPlayer, j, countTwo, candy)

if winner:
    print(f"Выиграл {onePlayer}")
else:
    print(f"Выиграл {twoPlayer}")