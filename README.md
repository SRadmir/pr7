# Это практическая работа №7 Варинат№2
## задание 1 ##
### код
```
n = int(input("Введите целое десятичное число x="));
print("В двоичную или восьмеричную систему?");
q = int(input("2 или 8 - "))
if n>=0:
    if q == 2:
        print(str(bin(n))[2:])
    elif q==8:
        print(str(oct(n))[2:])
    else:
        print("Неверно выбрали систему счисления")
else:
    if  q== 2:
        print('математическая запись  -',str(bin(n))[3:])
    elif q==8:
        print('математическая запись  -',str(oct(n))[3:])
    else:
        print("Неверно выбрали систему счисления")
        
```
## задание 2 ##
```
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
    
```
## задание 3 ##
```
a = float( input("a= "))
b = float( input("b= "))
c = float( input("c= "))
if b != 0:
    x = a/b - 2*c
    print(x)
else:
    print("неверное условие для b")
    
```