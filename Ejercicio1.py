import os
os.system("clear")
print("Bienvenido a tu programa de conversion de dinero")
valor=float(input("Ingrese la cantidad: "))
opcion=float(input("Ingrese la opcion de moneda a convertir:\n1.COP A USD \n2.USD A JPY \n3.JPY A COP: \n"))
copscon=valor/4000
usdcon=valor*144
yencon=valor*28
match opcion:
    case 1: 
        print(f"la conversion de pesos a dolares es: {copscon} USD")
    case 2:
        print(f"La conversion de dolares a yenes es: {usdcon} JPY")
    case 3:
        print(f"La conversion de yenes a pesos es: {yencon} COP")