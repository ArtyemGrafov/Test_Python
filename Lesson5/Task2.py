#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(data): 
    if not data: return ''

    result = '' 
    tmpChar = data[0] 
    count = 0 
    
    for char in data:
        if char != tmpChar: 
            result += str(count) + tmpChar 
            count = 1 
            tmpChar = char 
        else: 
            count += 1
     
    result += str(count) + tmpChar

    return result

def decode(data): 
    decode = '' 
    count = ''

    for char in data:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count) 
            count = ''
     
    return decode

def writeFile(data, fileName):
    with open(fileName, "w") as file:
        file.write(data)

def readFile(fileName):
    with open(fileName, "r") as file:
        return file.readline()

print("Encoding data...")
inputDecodingData = readFile("input_Task2_lesson5_decoding")
print("Input : " + inputDecodingData)
encodingData = encode(inputDecodingData)
print("Output : " + encodingData)
writeFile(encodingData, "output_Task2_lesson5_encoding")

print("Decoding data...")
inputEncodingData = readFile("input_Task2_lesson5_encoding")
print("Input : " + inputEncodingData)
decodingData = decode(inputEncodingData)
print("Output : " + decodingData)
writeFile(decodingData, "output_Task2_lesson5_decoding")
