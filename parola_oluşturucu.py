import random

Karakterler = "+-/*!&$#?=@_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("Şifre uzunluğunu giriniz."))

sifre = ""

for i in range(sifre_uzunlugu):

    sifre += random.choice(Karakterler)

print(sifre)