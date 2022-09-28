# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input("Enter n: "))

def intToBin(n):
    if n < 2: return str(n)
    return intToBin(n//2) + str(n - n//2 *2)
    """r = []
    while (n > 0):
        r.append(str(n - n//2 * 2))
        n //= 2
    #return bin(int("".join(list(reversed(r))), 2))
    return "".join(list(reversed(r)))"""

res = intToBin(num)

print(f"Int {num} => Bin {res}")