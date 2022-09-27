# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.


n = int(input("Enter n: "))
res = 0

coord = [[0 for j in range(n)] for i in range(2)]

for i in range(2):
    for j in range(n):
        coord[i][j] = int(input(f'Enter coord {j + 1} point {i + 1} : '))

if n == 1: print(f"Distance = {abs(coord[0][0] - coord[1][0])}")
else:
    for i in range(n):
        res += pow(coord[0][i] - coord[1][i], 2)
    print(f"Distance = {res ** (0.5)}")