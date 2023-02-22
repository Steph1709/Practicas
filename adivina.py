adivina = 0
turnos = 0

while adivina != 8 and turnos < 3:
    print("¿En que numero estoy pensando?")
    adivina = int(input())
    
    if adivina != 8:
        print("Te he ganado! Intenta de nuevo.")
        turnos = turnos + 1
    else:
        print("Lo has adivinado!")