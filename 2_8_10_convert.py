def get_source_base():
    while (True):
        try:
            sourceBase = int(input("Lütfen çevireceğiniz sayının tabanını giriniz: "))
        except ValueError:
            print("Geçerli bir tamsayı girmediniz. Lütfen yeniden deneyin.")
            continue
        if (sourceBase == 2 or sourceBase == 8 or sourceBase == 10):
            return str(sourceBase)
        else:
            print("Geçerli taban girmediniz. Geçerli tabanlar 2, 8 ve 10`dur. Lütfen yeniden deneyin.")


def get_target_base():
    while (True):
        try:
            targetBase = int(input("Lütfen sayının dönüştürüleceği hedef tabanı giriniz: "))
        except ValueError:
            print("Geçerli bir tamsayı girmediniz. Lütfen yeniden deneyin.")
            continue
        if (targetBase == 2 or targetBase == 8 or targetBase == 10):
            return str(targetBase)
        else:
            print("Geçerli taban girmediniz. Geçerli tabanlar 2, 8 ve 10`dur. Lütfen yeniden deneyin.")


def get_number(sourceBase):
    a = True
    while (a):
        try:
            number = int(input("Lütfen çevrilecek sayıyı giriniz: "))
        except ValueError:
            print("Geçerli bir tamsayı girmediniz. Lütfen yeniden deneyin.")
            continue

        number = str(number)
        listNumber = list(number)

        if (sourceBase == "10"):
            for i in listNumber:
                if i <= "9":
                    a = False
                    return number

                else:
                    print(sourceBase, "tabanında geçerli bir sayı girmediniz(", i, ">=", sourceBase,
                          "). Lütfen Yeniden deneyin")
                    break

        elif (sourceBase == "2") or (sourceBase == "8"):
            s = "i"

            for i in listNumber:
                if (i >= sourceBase):
                    s = "sikinti"
                    print(sourceBase, "tabanında geçerli bir sayı girmediniz(", i, ">=", sourceBase,
                          "). Lütfen Yeniden deneyin")
                    break

            if (s != "sikinti"):
                a = False
                return number


def convert_number(sourceBase, targetBase, number):
    if (sourceBase == "2" and targetBase == "10") or (sourceBase == "8" and targetBase == "10"):
        onluk = convert_base_to_10(number, sourceBase)
        return onluk
    elif (sourceBase == "2" and targetBase == "8") or (sourceBase == "8" and targetBase == "2"):
        onluk = convert_base_to_10(number, sourceBase)
        f = convert_10_to_base(onluk, targetBase)
        return f
    else:
        f = convert_10_to_base(number, targetBase)
        return f


def convert_base_to_10(number, base):
    if (base == "2" or base == "8"):
        intBase = int(base)
        intNumber = str(number)
        liste = list(intNumber)
        toplam = 0
        boyut = len(liste)
        for i in liste:
            i = int(i)
            toplam += i * (intBase ** (boyut - 1))
            boyut -= 1
        return toplam


def convert_10_to_base(number, targetBase):
    if (targetBase != "10"):
        a=""
        intNumber = int(number)
        intTargetBase = int(targetBase)
        while (intNumber > 0):
            kalan = intNumber % intTargetBase
            kalan=str(kalan)
            a=kalan+a
            intNumber //= intTargetBase
        return a


a = get_source_base()
b = get_target_base()
c = get_number(a)
d = convert_base_to_10(c, a)
e = convert_10_to_base(c, b)
f = convert_number(a, b, c)
print(f)
