# Bankamatik Uygulaması

EzgiHesap = {
    "ad" : "Ezgi Soydemir",
    "hesapNo" : "132456780",
    "bakiye" : 3000,
    "ekHesap" : 2000
}

SevgiHesap = {
    "ad" : "Sevgi Soydemir",
    "hesapNo" : "123456780",
    "bakiye" : 2000,
    "ekHesap" : 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"]>= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
    else :
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if(toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı (e/h)")

            if ekHesapKullanimi == "e":
                ekhesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapKullanilacakMiktar
                print("Paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print("Üzgünüz bakiyeniz yetersiz")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitinizde ise {hesap['ekHesap']} TL bulunmaktadır")

paraCek(EzgiHesap,3000)
bakiyeSorgula(EzgiHesap)

print("**********************")

paraCek(EzgiHesap,2000)
bakiyeSorgula(EzgiHesap)
