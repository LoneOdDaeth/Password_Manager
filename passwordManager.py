import os
import random
import string
from pyperclip import copy
from cryptography.fernet import Fernet
import controlPanel as control

def generateRandomPassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def cryptoPassword(length):
    content = generateRandomPassword(length)
    contentByte = content.encode('utf-8')
    encryptedContents = Fernet(key).encrypt(contentByte)
    
    return encryptedContents.decode('utf-8')

def decryptedPassword(content): 
    contentByte = content.encode('utf-8')
    decryptedContents = Fernet(key).decrypt(contentByte).decode()
    returnString = decryptedContents

    copy(returnString)
    return returnString

def savePassword(usrData, platform, length, key):

    cypherKey = key.decode('utf-8')
    printableData = cryptoPassword(length)

    with open(f"{usrData}/{platform}.key","a") as savePass:
        savePass.write(cypherKey + "\n" + printableData)

def readPassword(usrData, platform):
    lineList = []
    with open(f"{usrData}/{platform}.key","r") as readable:
        for line in readable:
            lineList.append(line.strip())

    decryptedPass = lineList[1]
    return decryptedPass

def showPassword(usrData, platform):
        lineList = []
        with open(f"{usrData}/{platform}.key","r") as readable:
            for line in readable:
                lineList.append(line.strip())

        readableKey = lineList[0]
        decryptedPass = lineList[1]

        textOrigin = Fernet(readableKey).decrypt(decryptedPass)
        copy(textOrigin.decode('utf-8'))
        return(textOrigin)

def listFile():
    filelist = []
    for fileName in os.listdir:
        filelist.append(filelist)
    print(filelist)

def interface(username):
    choose = int(input("Yeni şifre oluşturmak için 0.(sıfır)'ı, Mevcut şifreyi görüntülemek için 1'i tuşlayın: "))
    if choose == 0:
        global key
        key = Fernet.generate_key()
        length = int(input("Oluşturulacak şifrenin uzunluğunun kaç karakter olmasını istersiniz: "))
        platform = input("Şifre hangi platform için oluşturulacak: ")

        savePassword(username, platform, length, key)
        willDecryptedPass = readPassword(username, platform)
        print(decryptedPassword(willDecryptedPass))
        print("Şifre kopyalandı")

    else:
        listFile()
        file = input("Hangi platformun şifresini görüntülemek istiyorsunuz: ")
        print("Şifre kopyalandı")
        print(showPassword(username, file).decode("utf-8"))
        
