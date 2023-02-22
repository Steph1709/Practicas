a = int(input("Ingrese en valor de a: "))
b = int(input("Ingrese en valor de b: "))
c = int(input("Ingrese en valor de c: "))

raiz_positiva = (-b +(b * b - 4 * a * c) ** 0.5) / (2*a)
raiz_negativa = (-b -(b * b - 4 * a * c) ** 0.5) / (2*a)

print(raiz_positiva)
print(raiz_negativa)