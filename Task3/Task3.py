# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def getInt(msg):
    res = int(input(msg))
    if (res != 0): return res
    else: return getInt(msg)

x = getInt("Enter x: ")
y = getInt("Enter y: ")

if (x > 0 and y > 0): print("1")
if (x < 0 and y > 0): print("2")
if (x < 0 and y < 0): print("3")
if (x > 0 and y < 0): print("4")