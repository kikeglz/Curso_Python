# Programa para calcular el area de un cuadrado

# Area = L * L

lado = input("Ingresa el valor del lado:  ")  # input es para capturar lo que se escriba en teclado, lo que se escriba dentro del parentesis
                # se mostrara antes de donde se encuentra el cursor

lado = int(lado) #convertir string a entero

#area = lado * lado
area = lado ** 2

print(f"El area de tu cuadrado con valor l={lado} es: {area}")
