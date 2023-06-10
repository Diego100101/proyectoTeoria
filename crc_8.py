import sys
import binascii
from funciones import suma_xor, ascii_bin, verificaLlave, verificaTexto

# Código generador
# g(x) = x⁸ + x⁷ + x⁵ + x² + x + 1
# g(x) = 110100111
# Mayor exponente: 8

# -- Ecuaciones --
# prop = d(i) + C7
# C7 = prop + C6
# C6 = C5
# C5 = prop + C4
# C4 = C3
# C3 = C2
# C2 = prop + C1
# C1 = prop + C0
# C0 = prop

# Se socilita la cadena de caracteres
texto = input("Ingrese caracteres:\n")
verificaTexto(texto)

# Se socilita la llave de 8 bits
llave = input("Ingresa la llave de 8 bits:\n")
verificaLlave(llave)

# Define 8 unidades de memoria
unidades = ['C7', 'C6', 'C5', 'C4', 'C3', 'C2', 'C1', 'C0']

# Vector que une la llave y las unidades en un diccionario
vectorC = dict(zip(unidades, llave))
vectorC['prop'] = ''

# Almacena los valores anteriores de las unidades de memoria
vectorC_anterior = {'prop':'', 'C7':'', 'C6':'', 'C5':'', 'C4':'', 'C3':'', 'C2':'', 'C1':'', 'C0':''}
print(vectorC)

# Transforma la cadena de caracteres a binario
mensaje = ascii_bin(texto)[2:]

print(mensaje)

# Codificación
for i in mensaje:
    #prop = d(i) + C7
    vectorC['prop'] = suma_xor(i, vectorC['C7'])

    # C7 = prop + C6
    vectorC['C7'] = suma_xor(vectorC['prop'], vectorC['C6'])

    # C6 = C5
    vectorC['C6'] = vectorC['C5']

    # C5 = prop + C4
    vectorC['C5'] = suma_xor(vectorC['prop'], vectorC['C4'])

    # C4 = C3
    vectorC['C4'] = vectorC['C3']

    # C3 = C2
    vectorC['C3'] = vectorC['C2']

    # C2 = prop + C1
    vectorC['C2'] = suma_xor(vectorC['prop'], vectorC['C1'])

    # C1 = prop + C0
    vectorC['C1'] = suma_xor(vectorC['prop'], vectorC['C0'])

    # C0 = prop
    vectorC['C0'] = vectorC['prop']

#Codigo de redundancia
r = "".join([b for b in vectorC.values()])
r= (r[:-1])
print(r)

#Mensaje + CRC
Mens_CRC = mensaje,r
print(Mens_CRC)


