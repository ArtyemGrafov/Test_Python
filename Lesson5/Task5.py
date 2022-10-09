# Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]

list = [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] 
# list = [1, 5, 2, 1, 4, 6, 1, 8 , 15, 16, 17, 1, -1, -2, -3, -1, -5]

res = []
minElem = min(list)
maxElem = max(list)
tmp = [minElem]


while minElem < maxElem:
    minElem += 1
    if minElem in list:
        tmp.append(minElem)        
    else:
        res.append(tmp)        
        while minElem not in list or minElem == maxElem:
            minElem += 1
        tmp = [minElem]
        print(minElem)
res.append(tmp) 

maxLen = len(max(res, key=len))

[print([elem[0], elem[-1]]) for elem in res if len(elem) == maxLen]