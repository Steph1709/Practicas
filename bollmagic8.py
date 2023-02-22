import random

pregunta = input ('Realice su pregunta: ')

num_pregunta = random.randint(1, 9)

if num_pregunta == 1:
    r = 'Si, definitivamente.'
elif num_pregunta == 2:
    r = 'Es totalmente así.'
elif num_pregunta == 3:
    r = 'Sin duda.'
elif num_pregunta == 4:
    r = 'No entiendo tu pregunta, intenta de nuevo.'
elif num_pregunta == 5:
    r = 'Es mejor que aun no lo sepas.'
elif num_pregunta == 6:
    r = 'Mis fuentes dicen que no.'
elif num_pregunta == 7:
    r = 'El panorama no es el que esperas.'
elif num_pregunta == 8:
    r = 'Pregunta mas tarde.'
elif num_pregunta == 9:
    r = 'Es demasiado improbable.'
else:
    r = 'Lo siento no hay mas respuestas para ti.'
    
print('Pregunta: ' + pregunta)
print('Bola Magica 8: ' + r)  
