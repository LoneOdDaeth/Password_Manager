# kullanıcı adını ve şifresini tuttuğumuz dosyayı da şifreleyerek tutucaz
# şifre kontrolünü yaparken decrypted işlemini gerçekleştirmemiz lazım
import os
import getpass
from cryptography.fernet import Fernet
import passwordManager as passManage

def makeDir(usrData):
    os.mkdir(usrData)

def cryptoPassword(data, key):
    dataByte = data.encode('utf-8')
    encrptedData = Fernet(key).encrypt(dataByte)
    
    return encrptedData.decode('utf-8')

def cryptoPass(usrData, passData, key):
    cypherKey = key.decode('utf-8')
    passData = cryptoPassword(passData, key)
    with open(f"{usrData}/{usrData}.usr","a") as savePass:
        savePass.write(cypherKey + "\n" + passData)

def dosyaOlustur(usrData, passData):
    makeDir(usrData)
    key = Fernet.generate_key()
    cryptoPass(usrData, passData, key)
    
def checkUser(usrData, passData):
    Username = []
    for fileName in os.listdir():
        Username.append(fileName)
    if usrData in Username:
        checkPass(usrData, passData)
    else:
        print("Kullanıcı ismi bulunamadı.")
    
def checkPass(usrData, passData):
    lineList = []
    with open(f"{usrData}/{usrData}.usr","r") as readable:
        for line in readable:
            lineList.append(line.strip())
    
    readableKey = lineList[0]
    decryptedPassword = lineList[1]
    originPassword = Fernet(readableKey).decrypt(decryptedPassword).decode('utf-8')
    
    if passData != originPassword:
        print("Hatalı Şifre!!!")
    else:
        print(f"Hoşgeldiniz {usrData}")

def main():
    choose = int(input("Yeni kullanıcı için 0(sıfır)'ı, kullanıcı girişi için 1'i tuşlayınız."))
    global username
    username = input("Kullanıcı adı: ")
    password = getpass.getpass("Parola: ")
        
    if choose == 0:
        dosyaOlustur(username, password)
        print("Kullanıcı oluşturuldu")
    else:
        checkUser(username, password)
