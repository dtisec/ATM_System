import colorama
import os
import time

from colorama import Fore, Back, Style

colorama.init()
os.system('clear||cls')
time.sleep(0.5)

print(Fore.BLUE, "                    💲 PYTHON MERKEZ ATM 💲")

class ATM_Sistemi:
    def __init__(self, bakiye = 0):
        self.bakiye = bakiye

    def bakiye_sorgula(self):
        print(Fore.GREEN, "💰 Mevcut bakiyeniz: ", self.bakiye)
        return self.bakiye

    def para_yatir(self, tutar):
        self.bakiye += tutar
        print("Yatırılan tutar: ", tutar)
        print(Fore.GREEN, "💰 Mevcut bakiyeniz: ", self.bakiye)

    def para_cek(self, tutar):
        if self.bakiye >= tutar:
            self.bakiye -= tutar
            print("Çekilen tutar: ", tutar)
            print(Fore.GREEN, "💰 Mevcut bakiyeniz: ", self.bakiye)
        else:
            print(Fore.RED,"Yetersiz bakiye!")

atm = ATM_Sistemi(1000) # Buradan bakiyemizi belirleyebiliriz.

while True:
    print(Fore.BLUE, "1) Bakiye Sorgula")
    print(Fore.CYAN, "2) Para Yatır")
    print(Fore.MAGENTA, "3) Para Çek")
    print(Fore.RED, "4) Çıkış", Fore.RESET)
    
    secim = int(input(" Seçiminizi yapın:"))
    
    if secim == 1:
        atm.bakiye_sorgula()
    elif secim == 2:
        tutar = int(input("Yatırmak istediğiniz tutarı girin: "))
        atm.para_yatir(tutar)
    elif secim == 3:
        tutar = int(input("Çekmek istediğiniz tutarı girin: "))
        atm.para_cek(tutar)
    elif secim == 4:
        print("ATM kullandığınız için teşekkür ederiz. İyi günler!")
        break
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
