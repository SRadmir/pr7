ls = []
def qu(q):
    if (q == 0):
        return ls
    p = q % 4
    ls.append(p)
    qu(q // 4)
a = int(input("Введите целое, неорицательное число в десятичной системе счисления "))
if a==0:
        print('0')
elif a>0:
    qu(a)
    ls.reverse()
    chislo=int(str(ls)[1:-1].replace(', ',''))
    print(chislo)
else:
    print("Неверный ввод")
