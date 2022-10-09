# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def getLen(s):
    n = -1
    while(not s[n - 1].isalpha()):
        n -= 1
    return n

def checkWord(w):
    if "абв" in w:
        return "" if w[-1].isalpha() else w[getLen(w):]
               
    return w

text = "Я не согласен на забвение, хочу остаться незабвенным... незабвенным!"

print(" ".join([checkWord(word) for word in text.split(" ")]))