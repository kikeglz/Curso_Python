# Programa para solicitar datos y darles un formato para mostrarlos

nombre=input("Hola escribe tu nombre: \n")

edad=input("Ahora escribe tu edad: \n")

telefono=input("Cual es tu telefono? \n")

direccion=input("Ingresa tu dirección para enviarte un regalo: \n")

email=input("Escribe tu email para enviarte propaganda de coppel: \n")

nacionalidad=input("Indica tu nacionalidad: \n")

suscripcion_coppel = f"\t\t\t\t\tFormato de CREDITO COPPEL\nNombre: {nombre}\nEdad: {edad}\nTelefono: {telefono}\nDireccion: {direccion}\nEmail: {email}\nNacionalidad: {nacionalidad}.\n"
mensaje_aprobacion = f"Gracias por solicitar tu credito coppel {nombre}, al validar tus datos como tu edad que actualmente tienes {edad} años, nacionalidad: {nacionalidad} y tu dirección: {direccion}\nEs de nuestro agrado informarte que tu línea de crédito fue aprobada y esta lista para usarse."
print(suscripcion_coppel)
print(mensaje_aprobacion)