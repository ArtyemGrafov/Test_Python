# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

arr = [2, 3, 5, 9, 3]

# print(f"Result = {sum([val for key, val in enumerate(arr) if key%2])}")

res = 0

for i in range(len(arr)):
    if i%2 != 0: res += arr[i]

print(f"Result = {res}")