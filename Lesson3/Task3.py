# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr = [1.1, 1.2, 3.1, 5, 10.01]

tmpArr = [str(float(elem)).split(".")[1] for elem in arr]

maxLen = max(map(lambda x: len(x), tmpArr)) 

resArr = [int(elem) * 10 ** (maxLen - len(elem)) for elem in tmpArr if elem != "0"]

print(f"Result = {(max(resArr) - min(resArr)) / 10 ** maxLen}")