# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def getName(msg):
    return input(f"Emter {msg} name: ")

def getInt(msg, max):
    while True:
        try:
            n = int(input(msg))
            if 0 < n <= max:
                return n
            else:
                print(f"Not in range [1, {max}]. One more ...")
        except Exception:
            print("Not int! One more ...")

def getFirst(name1, name2):
    one = randint(1, 6)
    two = randint(1, 6)
    if one == two: getFirst(name1, name2)
    if one > two: print("First - " + name1)
    else: print("First - " + name2)
    return one > two

def makeMove(name, nextMove):
    global candies

    if candies > 28: max = 28
    else: max = candies

    candies -= getInt(f"Take candies {name} : ", max)
    print(f"Remained {candies} candies")

    if nextMove == 0: nextMove = 1
    else: nextMove = 0
    return nextMove

def makeMoveRandom(nextMove):
    global candies

    if candies > 28:
        n = randint(1, 28)
    else: 
        n = candies
    print(f"Take candies bot : {n}")    

    candies -= n
    print(f"Remained {candies} candies")

    if nextMove == 0: nextMove = 1
    else: nextMove = 0   
    return nextMove

def PvP():
    namePlayer1 = getName("player1")
    namePlayer2 = getName("player2")
    
    if getFirst(namePlayer1, namePlayer2):
        move = 0
        while candies > 0:
            move = makeMove(namePlayer1, move)
            if candies > 0:
                move = makeMove(namePlayer2, move)            
    else:
        move = 1
        while candies > 0:
            move = makeMove(namePlayer2, move)
            if candies > 0:    
                move = makeMove(namePlayer1, move)            

    if move == 1: print(namePlayer1 + " win!")
    else: print(namePlayer2 + " win!")

def PvB():
    namePlayer1 = getName("player1")
    namePlayer2 ="bot"
    
    if getFirst(namePlayer1, "bot"):
        move = 0
        while candies > 0:
            move = makeMove(namePlayer1, move)
            if candies > 0:
                move = makeMoveRandom(move)            
    else:
        move = 1
        while candies > 0:
            move = makeMoveRandom(move)
            if candies > 0:    
                move = makeMove(namePlayer1, move)            

    if move == 1: print(namePlayer1 + " win!")
    else: print(namePlayer2 + " win!")

candies = 2021

s = input("Selekt mode(1 - PvP, 2 - PvB) : ")
if s == "1": PvP()
elif s == "2": PvB()
else: print("Error")