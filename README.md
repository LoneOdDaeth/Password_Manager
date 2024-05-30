# Şifre Yöneticisi

Bu Python betiği, cryptography kütüphanesinden Fernet şifreleme yöntemini kullanarak çeşitli platformlar için şifreler oluşturma, şifreleri şifreleme, şifreleri çözme, kaydetme ve geri alma işlevleri sağlar.

## Özellikler

- Belirtilen uzunluklarda rastgele şifreler oluşturma.
- Fernet şifreleme kullanarak şifreleri şifreleme.
- Farklı platformlar için şifreleri şifreli olarak kaydetme.
- Belirli platformlar için şifreleri geri alıp çözme.

## Gereksinimler

- Python 3.x
- cryptography kütüphanesi (`pip install cryptography`)

## Kullanım

1. **Şifre Oluşturma ve Kaydetme:**

   Betiği çalıştırın ve belirli bir platform için bir şifre oluşturup kaydetmek için seçenek 0'ı seçin.
   

2. **Şifreleri Geri Alma ve Çözme:**

    Betiği çalıştırın ve belirli bir platform için bir şifreyi geri alıp çözmek için seçenek 1'i seçin.


## Güvenlik Notu

- Şifreleme anahtarınızı (`key.key`) güvende tutun ve kimseyle paylaşmayın.
- Şifreleri kaydetmek için kullanılan platform isimlerini hatırlamak önemlidir çünkü bunlar geri almak için gereklidir.

## Katkıda Bulunanlar

- [LoneOdDaeth](https://github.com/LoneOddaeth)

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - ayrıntılar için (LICENSE) dosyasına bakınız.

---

# Password Manager

This Python script provides functionalities to generate, encrypt, decrypt, save, and retrieve passwords for various platforms using the Fernet encryption method from the cryptography library.

## Features

- Generate random passwords with specified lengths.
- Encrypt passwords using Fernet encryption.
- Save encrypted passwords for different platforms.
- Retrieve and decrypt passwords for specific platforms.

## Requirements

- Python 3.x
- cryptography library (`pip install cryptography`)

## Usage

1. **Generating and Saving Passwords:**

   Run the script and choose option 0 to generate and save a password for a specific platform.
   

2. **Retrieving and Decrypting Passwords:**

    Run the script and choose option 1 to retrieve and decrypt a password for a specific platform.


## Security Note

- Keep your encryption key (`key.key`) safe and do not share it with anyone.
- Make sure to remember the platform names used for saving passwords as they are needed for retrieval.

## Contributors

- [LoneOdDaeth](https://github.com/LoneOdDaeth)

## License

This project is licensed under the MIT License - see the (LICENSE) file for details.

