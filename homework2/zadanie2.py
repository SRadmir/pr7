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
        print('-',str(bin(n))[3:])
    elif q==8:
        print('-',str(oct(n))[3:])
    else:
        print("Неверно выбрали систему счисления")
        

