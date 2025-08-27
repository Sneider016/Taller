import os
os.system("clear")
print("Bienvenido a su programa de tablas de multiplicar")
numero=int(input("Ingrese el numero deseado entre 1 y 10: \n"))
tabla=numero
inicio=1
while inicio <= 10:
    resultado = tabla * inicio
    print(tabla,"*",inicio,"=",resultado)
    inicio += 1