# Programa para pedir un numero del 1 al 1024 y convertirlo a ascii

num = input("Escribe el número que deseas convertir a binario que este entre 1 y 1024: \n")
num = int(num)
binario = format(num, "b")

print(f"El número: {num} convertido a binario es: {binario}")