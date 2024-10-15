# Это практическая работа №7 Варинат№2
## задание 1 ##
### код
```
n = int(input("Введите целое десятичное число x= "));
print("В двоичную или восьмеричную систему?");
q = int(input("2 или 8  "))
if q == 2:
    n= str(bin(n))[2:]
    print(n)
elif q==8:
    n= str(oct(n))[2:]
    print(n)
else:
    print("Ошибка(неправильно выбрали систему счисления)")
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