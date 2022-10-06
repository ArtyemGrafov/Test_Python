# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def getMinMultiplier(n):
    multiplier = 2
    while multiplier <= n:
        if n%multiplier == 0: 
            return multiplier
        else:
            multiplier += 1

def getSimpleMultipliers(n):
    listN = []
    while n > 1:        
        multiplier = getMinMultiplier(n)
        listN.append(multiplier)
        n = n // multiplier
    return listN

# num = 83006 # 2 * 7 * 7 * 7 * 11 * 11
try:
    print(getSimpleMultipliers(int(input("Enter n: "))))
except Exception:
    print("Enter INT")