from pysimplesoap.helpers import double

print("Ejercicio11")
# Antes de trabajar con numeros pasados por parámetro habrá que convertirlo a int, double o float
a = float(input("Introduzca un numero: "))
b = float(input("Introduzca otro numero: "))
c = input("Introduzca: restar, sumar, multiplicar o dividir: ")
if c == "restar":
    print(a - b)
elif c == "sumar":
    print(a + b)
elif c == "multiplicar":
    print(a * b)
elif c == "dividir":
    if a != 0 or b != 0:
        if a > b:
            print(a / b)
        else:
            print(b / a)
else:
    print("Error al escribir el operando deseado")