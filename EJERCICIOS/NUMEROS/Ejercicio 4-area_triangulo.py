# Programa para calcular la area de un triangulo
# area = (base * altura)/2

base=input("Escribe la base del triangulo: ")
base=float(base)

altura=input("Escribe la altura del triangulo: ")
altura=float(altura)

area=(base*altura)/2

print(f"El area de un triangulo con altura de: {altura} y base de: {base}\nEs igual a: {area}")