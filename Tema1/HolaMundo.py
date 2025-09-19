"""Introduccion a Python
este es un comentario
de varias lineas"""
# Este es un comentario de una sola linea
print("Hola Mundo")
print("El weta " * 4)

#Tipos de datos
print(type(3.5))
print(type(True))
print(type("Hola"))
print(type([1, 2, 3]))

numero = 100
cadena = 10.5
booleano = False

print(numero)
print(cadena)
print(booleano)

print(type(numero))
print(type(cadena))
print(type(booleano))

#El tipo de dato de una variable puede cambiar
numero = "Ahora soy una cadena"
print(numero)
print(type(numero))

numero, contador, acumulador = 10, 20, 30
mensa1, mensa2 = "Hola", "Mundo"
print(numero, contador, acumulador)
print(mensa1, mensa2)
print(reversed("Hola Mundo"))

area = 3.14 * pow(5, 2)
print("El area del circulo es: ", area)

#la funcion str() convierte a String
numero_str = str(numero)
print(type(numero_str))
print(numero_str)

# para saber la longitud usaremos la funcion len()
print(len(mensa1))

#Para pedir por teclado usaremos input() -> siempre devuelve un String
nombre = input("Cual es tu nombre? ")
print("Hola " + nombre)
edad = input("Cual es tu edad? ")
print("Tu edad es " + edad)
print(type(edad))
# Si queremos que la edad sea un numero usaremos int()
edad = int(input("Cual es tu edad? "))
print("Tu edad es " + str(edad))
print(type(edad))