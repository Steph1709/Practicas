yuan = int(input("¿Cuantos yuanes tienes? =  "))
yen = int(input("¿Cuantos yenes tienes? =  "))
won = int(input("¿Cuantos wones tienes? =  "))

yean_dolar = yuan * 0.15
yen_dolar = yen * 0.0076
won_dolar = won * 0.00080

dolares = yean_dolar + yen_dolar + won_dolar

print(dolares)