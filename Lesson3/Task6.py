# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

# F(-n) = (-1) ** (n + 1) * F(n)

k = int(input("Enter n: "))

arrPositiveSeq = [0, 1]
arrNegativeSeq = []

for i in range(1, k):
    arrPositiveSeq.append(arrPositiveSeq[i] + arrPositiveSeq[i - 1])

for i in range(1, k + 1):
    arrNegativeSeq.append((-1)**i * arrPositiveSeq[-i])

print(f"Result = {arrNegativeSeq + arrPositiveSeq}")