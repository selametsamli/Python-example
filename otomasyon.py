import sqlite3

while True:
    print("Görüntülemek için 1 \nÖğrenci Eklemek için 2\nÇıkam için '-1'")
    secim=int(input("Seçim yapınız:"))

    if secim==1:
        vt = sqlite3.connect('otomasyon.sqlite')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogrenci_bilgileri""")
        veriler=im.fetchall()
        print (veriler)

    elif secim==2:
        vt=sqlite3.connect("otomasyon.sqlite")
        im=vt.cursor()
        while 1:
            ogrenci=input("Öğrenci eklemek için 'e' çıkış için 'q': ")
            if ogrenci=="e":
                ogrenci_adi=input("Öğrenci Adını Girin: ")
                ogrenci_soyadi=input("Öğrenci Soyadı Girin: ")
                ogrenci_tcno=str(input("Öğrenci TC Numarasını Girin: "))
                ogrenci_no=str(input("Öğrenci Numarası Girin: "))
                ogrenci_telno=str(input("Öğrenci Telefon Numarası girin: "))
                im.execute("""CREATE TABLE IF NOT EXISTS
                    ogrenci_bilgileri (Ad,Soyad,Tc,Numara,TelefonNo)""")
                im.execute("""INSERT INTO ogrenci_bilgileri VALUES
                    (?,?,?,?,?)""",(ogrenci_adi,ogrenci_soyadi,ogrenci_tcno,ogrenci_no,ogrenci_telno))
                vt.commit()

            elif ogrenci=="q":
                break
            else:
                print("Hatalı Giriş Yaptınız.")
    elif secim==-1:
        break