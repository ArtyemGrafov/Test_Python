# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr = [1.1, 1.2, 3.1, 5, 10.01]

"""tmpArr = [str(float(elem)).split(".")[1] for elem in arr]

maxLen = max(map(lambda x: len(x), tmpArr)) 

resArr = [int(elem) * 10 ** (maxLen - len(elem)) for elem in tmpArr if elem != "0"]

print(f"Result = {(max(resArr) - min(resArr)) / 10 ** maxLen}")"""

def maxLenElem(n):
    max = len(n[0])
    for i in range(1, len(n)):
        if max < len(n[i]): max = len(n[i])
    return max

tmpArr = []

for elem in arr:
    tmpArr.append(str(float(elem)).split(".")[1])

resArr = []
maxLen = maxLenElem(tmpArr)

for s in tmpArr:
    if s != "0":
        resArr.append(int(s) * 10**(maxLen - len(s)))

print(f"Result = {(max(resArr) - min(resArr)) / 10 ** maxLen}")