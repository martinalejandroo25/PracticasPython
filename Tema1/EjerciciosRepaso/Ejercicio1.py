"""Introduccion a Python"""
#Realiza un programa que vaya pidiendo numeros enteros mientras no introduzcas el -1.
# Como resultado debe devolver la cantidad de numeros introducidos y la suma de esos numeros.
ACTUAL = 0
NUM = 0
CONTA = 0
while ACTUAL != -1:
    ACTUAL = int(input("Dame un numero,escribe -1 para finalizar "))
    if ACTUAL  != -1:
        NUM += ACTUAL
        CONTA   += 1
print("La suma de los numeros introducidos es: " + str(NUM))
print("La cantidad de numeros introducidos es: " + str(CONTA))
