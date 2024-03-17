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

def savePassword(platform, length):
    with open(f"{platform}.key","a") as savePass:
        savePass.write(cryptoPassword(length))

def readPassword(platform):
    with open(f"{platform}.key","r") as readable:
        willDecryptedPass = readable.read()
    
    return willDecryptedPass

key = Fernet.generate_key()

length = int(input("What is the character length of the password to be created: "))
platform = input("For which platform will the password be created: ")

print(savePassword(platform, length))
willDecryptedPass = readPassword(platform)
print(decryptedPassword(willDecryptedPass))