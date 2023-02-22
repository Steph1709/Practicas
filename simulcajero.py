#Cambio de contraseña de tarjeta en un cajero automatico.

print("Cajero del banco")

clave = int(input("Ingrese su clave de 4 digitos: "))
clave2 = 0

while clave != 1234:
    clave = int(input("Clave incorrecta. Ingrese su clave de nuevo o comuniquese con el banco emisor: "))

if clave == 1234:
    clave = int(input("Ingrese su nueva clave: "))
    print("Clave actualizada. Gracias por usar nuestro servicio de cajero automatico")