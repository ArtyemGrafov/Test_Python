# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

array = [[1, 4, 7, 2], [5, 9, 10, 3]]
tmpArray = []

print(*array)

for rows in array:
    for num in rows:
        tmpArray.append(num)


for i in range(len(tmpArray) - 1):
    for j in range(i + 1, len(tmpArray)):
        if tmpArray[i] > tmpArray[j]:
            tmpArray[i], tmpArray[j] = tmpArray[j], tmpArray[i]

k = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = tmpArray[k]
        k += 1



print(*array)