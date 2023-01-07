import string
import random

#  Function to encode
def encoding():
    encodedList = []
    randomWord = ""
    encodedStr = ""

    strToEncode = input("Input a string to encode: ")
    strList = strToEncode.split()

    for word in strList:
        if (len(word) < 3):
            encodedList.append(word[::-1])
        else:
            randStr1 = "".join(random.choice(
                string.ascii_letters+string.digits)for i in range(3))
            randStr2 = "".join(random.choice(
                string.ascii_letters+string.digits)for i in range(3))
            randomWord = randStr1+word[1:len(word)]+word[0]+randStr2
            encodedList.append(randomWord)

    for item in encodedList:
        encodedStr += " "+item
    print(encodedStr)

# Function to decode
def decoding():
    decodedStr = ""
    decodedList = []

    strToDecode = input("Input a string to decode: ")
    strList = strToDecode.split()

    for word in strList:
        if (len(word) < 3):
            decodedList.append(word[::-1])
        else:
            decodedWord = word[-4]+word[3:len(word)-4]
            decodedList.append(decodedWord)

    for item in decodedList:
        decodedStr += " "+item
    print(decodedStr)

# Code to create a menu
while (1):
    print("""
    What you want to choose?
    \t 1. Encoding
    \t 2. Decoding
    \t 3. Exit
    """)
    choice = input("Input your choice: (1/2/3): ")
    match choice:
        case "1":
            encoding()
        case "2":
            decoding()
        case "3":
            break
        case _:
            print("Invalild selection!!!\nPlease try again")
