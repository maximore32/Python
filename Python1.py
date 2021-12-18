edad=input("Dinos tu edad: ")

while(edad.isdigit()== False):
    print("Favor de introducir valor númerico")
    edad=input("Dinos tu edad: ")

if(int(edad)<18):
    print("Usted es menor de edad, no puede ingresar")
else:
    print("Bienvenido Señor")


print("Usted a ingresado su edad de: "+edad+" años")


def suma(a,b):
    resultado= a+b
    return resultado

suma(5,5)