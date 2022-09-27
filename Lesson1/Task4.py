# Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") 
# и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

operations = ["+", "-", "*", "/", "mod", "pow", "div"]

x = float(input("Enter first num: "))
y = float(input("Enter second num: "))

print("Enter operation from available: ")
print(*operations, sep=", ")
operation = input("Operation: ")

if (operation not in operations): print("Not available.")
else:
    match operation:
        case "+":
            print(x + y)
        case "-":
            print(x - y)
        case "*":
            print(x * y)
        case "/":
            if (y == 0): print("Division dy zero!")
            else: print(x / y)
        case "mod":
            if (y == 0): print("Division dy zero!")
            else: print(x % y)
        case "div":
            if (y == 0): print("Division dy zero!")
            else: print(int(x /y))
        case "pow":
            print(pow(x, y))