# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

import random

def getSize():
    m, n = 1, 1
    while m * n % 2 != 0:
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))
    return m, n

def printArray(a, msg):
    print(msg)
    for e in a:
        for s in e:
            print(str(s).ljust(4), end=" ")
        print()

def shuffleArray(a):
    temArr = [elem for ai in a for elem in ai]
    usedIndexes = []
    i = 0
    while len(usedIndexes) < len(temArr) // 2:
        index = random.randint(len(temArr) // 2, len(temArr) - 1)
        if index not in usedIndexes:
            temArr[i], temArr[index] = temArr[index], temArr[i]
            i += 1
            usedIndexes.append(index)
    return [temArr[i:i+len(a[0])] for i in range(0, len(temArr), len(a[0]))]

arr = []

a, b = getSize()

arr = [[random.randint(1, 100) for i in range(a)] for j in range(b)]

printArray(arr, "Random array:")

printArray(shuffleArray(arr), "Shuffled Array:")