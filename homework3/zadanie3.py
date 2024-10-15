ls = []
def qu(q):
    if (q == 0):
        return ls
    p = q % 4
    ls.append(p)
    qu(q // 4)
a = int(input("Введите целое число в десятичной системе счисления "))
if a==0:
        print('0')
if a>0:
    qu(a)
    ls.reverse()
    chislo=int(str(ls)[1:-1].replace(', ',''))
    print(chislo)
else:
    a*=-1
    qu(a)
    ls.reverse()
    chislo=int(str(ls)[1:-1].replace(', ',''))
    print("математическая запись: -",chislo)
    
