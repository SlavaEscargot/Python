tex = open(r'/home/slava/Рабочий стол/zadanie_17.txt')
maxnambre = -9999
for namber in tex:
    namber16 = int(namber)
    namber16 = (hex(namber16))
    if ((namber16[-1]) == 'e') and (maxnambre < namber16) :
        maxnambre = namber16
print(maxnambre)