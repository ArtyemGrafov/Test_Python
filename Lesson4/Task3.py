# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def degreeToStr(val):
    base = ["⁰", '¹', "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    if val < 10:
        return base[val]
    else: 
        return degreeToStr(val//10) + base[val%10]

def getPolynomial(coeff, e):
    str = ""
    for i in range(len(coeff)):
        if coeff[i] != 0:
            if len(coeff) - 1 - i > 1: 
                if coeff[i] == 1: str += f"*x{degreeToStr(e-i)} + "
                else: str += f"{coeff[i]}*x{degreeToStr(e-i)} + "
            if len(coeff) - 1 - i == 1:
                if coeff[i] == 1: str += f"x + "
                else: str += f"{coeff[i]}*x + "
            if len(coeff) - 1 - i == 0: str += f"{coeff[i]} "
    return str + "= 0"

try:
    k = int(input("Enter degree: "))

    coefficients = [random.randint(1, 100)]
    coefficients.extend([random.randint(0, 100) for i in range(k)])

    strPolin = getPolynomial(coefficients, k)

    with open("output_Task3_Lesson4", "w", encoding="utf-16") as file:
        #file.write(f'Coeff : {str(coefficients)}\n')
        file.write("result : " + strPolin)
    print("Done")
except Exception:
    print("Error")