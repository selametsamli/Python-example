def get_source_base():
    while (True):
        try:
            sourceBase = int(input("Please enter the base of the number you will convert: "))
        except ValueError:
            print("You have not entered a valid integer. Please try again.")
            continue
        if (sourceBase == 2 or sourceBase == 8 or sourceBase == 10):
            return str(sourceBase)
        else:
            print("You have not entered a valid base. Valid bases are 2, 8 and 10. Please try again.")


def get_target_base():
    while (True):
        try:
            targetBase = int(input("Please enter the target base where the number will be converted: "))
        except ValueError:
            print("You have not entered a valid integer. Please try again.")
            continue
        if (targetBase == 2 or targetBase == 8 or targetBase == 10):
            return str(targetBase)
        else:
            print("You have not entered a valid base. Valid bases are 2, 8 and 10. Please try again.")


def get_number(sourceBase):
    a = True
    while (a):
        try:
            number = int(input("Please enter the number to be translated: "))
        except ValueError:
            print("You have not entered a valid integer. Please try again.")
            continue

        number = str(number)
        listNumber = list(number)

        if (sourceBase == "10"):
            for i in listNumber:
                if i <= "9":
                    a = False
                    return number

                else:
                    print(sourceBase, "You have not entered a valid number in Base(", i, ">=", sourceBase,
                          ").Please try again")
                    break

        elif (sourceBase == "2") or (sourceBase == "8"):
            s = "i"

            for i in listNumber:
                if (i >= sourceBase):
                    s = "sikinti"
                    print(sourceBase, "You have not entered a valid number in Base(", i, ">=", sourceBase,
                          "). Please try again")
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
        total = 0
        size = len(liste)
        for i in liste:
            i = int(i)
            total += i * (intBase ** (size - 1))
            size -= 1
        return total


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
