# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

arr = [2, 3, 4, 5, 6]
# arr = [2, 3, 5, 6]

# res = [arr[i] * arr[len(arr) - 1 - i] for i in range(int((len(arr) + 1) / 2))] #

res = []

for i in range(int((len(arr) + 1) / 2)):
    res.append(arr[i] * arr[len(arr) - 1 - i])

print(f"Result = {res}")