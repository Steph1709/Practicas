# Sombrero seleccionador

Gryffindor = 0 
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Bienvenido a tu primer paso para entrar en Hogwarts")

print("A continuacion se le haran unas preguntas, por favor seleccione su respuesta con el numero correspondiente")

# Pregunta 1
print()
print("¿Que prefiere, el Amanecer o el Anochecer?")
print("1) Amanecer")
print("2) Anochecer")
respuesta = int(input())

if respuesta == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif respuesta == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Respuesta invalida")

#pregunta 2
print()
print("Quiero ser recordado como una persona: ")
print("1) Buena")
print("2) Sabia")
print("3) Audaz")
print("4) Grande")
respuesta = int(input())

if respuesta == 1:
    Hufflepuff += 1
elif respuesta == 2:
    Ravenclaw += 1
elif respuesta == 3:
    Gryffindor += 1
elif respuesta == 4:
    Slytherin += 1
else:
    print("Respuesta invalida")

#pregunta 3
print()
print("Cual de los siguientes instrumentos produce un sonido mas agradable para usted ")
print("1) El violin")
print("2) La trompeta")
print("3) El piano")
print("4) El tambor")
respuesta = int(input())

if respuesta == 1:
    Slytherin + 1
elif respuesta == 2:
    Hufflepuff += 1
elif respuesta == 3:
    Ravenclaw += 1
elif respuesta == 4:
    Gryffindor += 1
else:
    print("Respuesta invalida")

if Slytherin >= Hufflepuff and Slytherin >= Ravenclaw and Slytherin >= Gryffindor:
    print("Felicidades, su casa es... Slytherin")
elif Hufflepuff >= Ravenclaw and Hufflepuff >= Gryffindor and Hufflepuff >= Slytherin:
    print("Felicidades, su casa es... Hufflepuff")
elif Ravenclaw >= Gryffindor and Ravenclaw >= Slytherin and Ravenclaw >= Hufflepuff:
    print("Felicidades, su casa es... Ravenclaw")
elif Gryffindor >= Slytherin and Gryffindor >= Hufflepuff and Gryffindor >= Ravenclaw:
    print("Felicidades, su casa es... Gryffindor")