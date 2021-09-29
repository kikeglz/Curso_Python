# Programa que pide un valor en grados centigrados y lo muestra en farenheit
#(0°C * 9/5)+32 = °F

celsius = input("Escribe los grados Celcius que deseas convertir: ")
celsius = float(celsius)

conversion = (celsius * 9/5)+32

print(f"{celsius}°C es igual a: {conversion}°F")