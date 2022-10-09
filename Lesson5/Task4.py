# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def degreeToUtf_8(val):
    base = ["⁰", '¹', "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    res = ""    
    for i in range(len(val)):
        res += str(base.index(val[i]))    
    return res

def degreeToStr(val):
    base = ["⁰", '¹', "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    if val < 10:
        return base[val]
    else: 
        return degreeToStr(val//10) + base[val%10]

def listToDict(list):
    dict_res = {}
    for elem in list:
        if "*x" in elem:
            mult = int(elem.split("*x")[0])
            if elem.split("*x")[1] != "":
                degree = degreeToUtf_8(elem.split("*x")[1])
            else:
                degree = "1"
        else:
            mult = int(elem)
            degree = "0"
        dict_res[degree] = mult
    return dict_res

def mergDict(d1, d2):
    for key in d2.keys():
        if key in d1.keys():
            d2[key] += d1[key]
    return(d1 | d2)

def writeFile(data, fileName):
    with open(fileName, "w", encoding="utf-16") as file:
        file.write(data)

def readFile(fileName):
    with open(fileName, "r", encoding="utf-16") as file:
        return file.readline()

def dictToPolin(d):
    res = ""
    for k in dict1.keys():
        if k == "0" and dict1[k] != 0: res += str(dict1[k])
        elif k == "1" and dict1[k] != 0:
            if dict1[k] == 1: res += "x + " 
            else: res += f"{dict1[k]}*x + "
        elif dict1[k] != 0:
            res += f"{dict1[k]}*x{degreeToStr(int(k))} + "
    return (res + " = 0")


polinomial = readFile("input1_Task4_lesson5")
dict1 = listToDict([i for i in polinomial.split()[:-2] if i != "+"])

polinomial = readFile("input2_Task4_lesson5")
dict2 = listToDict([i for i in polinomial.split()[:-2] if i != "+"])

writeFile(dictToPolin(mergDict(dict1, dict2)), "output_Task4_Lesson5")