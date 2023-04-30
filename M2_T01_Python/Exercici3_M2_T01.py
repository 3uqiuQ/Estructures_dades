import random

numeros = [random.randint(0, 99) for _ in range(50)]
print(type(numeros))
print(*numeros)

# Quants números hi ha?
cant = len(numeros) 
print('\nHi han ' + str(cant) + ' números a la llista.\n')

# Quantes vegades apareix el número 3?
cant3 = numeros.count(3)
print('El número 3 apareix ' + str(cant3) + ' vegades ala llista.\n')

# Quantes vegades apareixen els nombres 3 i 4?
cant3_4_1 = numeros.count(3)
cant3_4_2 = numeros.count(4)
print('los números 3 i 4  apareixen ' + str(cant3_4_1 + cant3_4_2) + ' vegades ala llista.\n')

# Quin és el número més gran?
gr = max(numeros)
print('El número més gran de la llista es el ' + str(gr) + '.\n')

# Quins són els 3 números més petits?
ord = sorted(numeros)
petit3 = ord[:3]
print(f'Els 3 números més petits de la llista son: ' + str(petit3) + '.\n')

# Quin és el rang d’aquesta llista?
rango = max(numeros) - min(numeros)
print('El rang de la llista es ' + str(rango) + '.\n')


