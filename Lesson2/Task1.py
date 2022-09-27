# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# print(sum(map(int, str(abs(float(input("Enter num: ")))).replace(".", ""))))

def getSumDigits(n):    
    if n < 10:
        return n
    else:
        return n % 10 + getSumDigits(n // 10)

num = abs(float(input("Enter num: ")))

while (num % 1 != 0):
    num *= 10

print(f"Sum digits = {int(getSumDigits(num))}")