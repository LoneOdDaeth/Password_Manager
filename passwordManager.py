# istenilen dosyadaki veriyi decrpt etmek için anahtarı da dosyaya kaydedip veriyi almamız lazım
import os
import random
import string
from cryptography.fernet import Fernet

def generateRandomPassword(length): # create the random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    # print(password)

    return password

def cryptoPassword(length): # encrypt the created password
    content = generateRandomPassword(length)
    contentByte = content.encode('utf-8') # Converting incoming data in string structure to byte
    encryptedContents = Fernet(key).encrypt(contentByte) # This is where the encryption happens
    
    return encryptedContents.decode('utf-8') # Converting incoming data in byte structure to string and return the string

def decryptedPassword(content): # decrypt the encrypted password
    contentByte = content.encode('utf-8')
    decryptedContents = Fernet(key).decrypt(contentByte).decode()
    returnString = decryptedContents

    return returnString

def savePassword(platform, length, key):

    cypherKey = key.decode('utf-8')
    printableData = cryptoPassword(length)

    with open(f"{platform}.key","a") as savePass:
        savePass.write(cypherKey + "\n" + printableData)

def readPassword(platform):
    lineList = []
    with open(f"{platform}.key","r") as readable:
        for line in readable:
            lineList.append(line.strip())

    decryptedPass = lineList[1]
    return decryptedPass

def showPassword(platform):
        lineList = []
        with open(f"{platform}.key","r") as readable:
            for line in readable:
                lineList.append(line.strip())

        readableKey = lineList[0]
        decryptedPass = lineList[1]

        textOrigin = Fernet(readableKey).decrypt(decryptedPass)
        return(textOrigin)

choose = int(input("What do you want? Decrypted[1] or Creat the password[0]."))
if choose == 0:
    key = Fernet.generate_key()
    length = int(input("What is the character length of the password to be created: "))
    platform = input("For which platform will the password be created: ")

    savePassword(platform, length, key)
    willDecryptedPass = readPassword(platform)
    print(decryptedPassword(willDecryptedPass))

else:
    file = input("Enter the file name: ")
    print(showPassword(file))
