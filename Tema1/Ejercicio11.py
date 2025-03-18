# 11. Realiza un programa que calcule el área y el perímetro de un círculo de radio 3,6 metros.
import math


print("Calcular Area y Perimetro de un circulo")
print("el radio es de 3,6m")
area = float(math.pi * math.pow(3.6,2))
print("El area de la circunferencia es de " + str(area))
perimetro = float(2 * math.pi * 3.6)
print("El perimetro de la circunferencia es de " + str(perimetro)) 
# para imprimir un resultado junto con un mensaje se deberá convertir a str(resultado)