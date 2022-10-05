# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def isPrime(x):
    if x == 1: return False
    else:
        count = 2
        for i in range(2, x):
            if x%i == 0: count += 1
    return count == 2

def getDivisors(a):
    res = []                         # [i for i in range(2, n+1) if n%i == 0 and isPrime(i)]
    for i in range(2, a + 1):
        if a%i == 0 and isPrime(i):
            res.append(i)
    return res

try:
    n = int(input("Enter n: "))
    print(f"result = {getDivisors(n)}")
except Exception:
    print("Enter INT")