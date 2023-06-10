import sys
import binascii
from funciones import suma_xor, ascii_bin, verificaLlave, verificaTexto, bin_ascii

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

# Se socilita la cadena de caracteres D(x)
texto = input("Ingrese caracteres:\n")
verificaTexto(texto)

# Se socilita la llave de 8 bits
#llave = input("Ingresa la llave de 8 bits:\n")
llave = '010'
verificaLlave(llave)

# Define 8 unidades de memoria
unidades = ['C2', 'C1', 'C0']# 'C5', 'C6', 'C7']

# Vector que une la llave y las unidades en un diccionario
vectorC = dict(zip(unidades, llave))
vectorC['prop'] = ''

# Almacena los valores anteriores de las unidades de memoria
vectorC_anterior = {'prop':'', 'C2':'', 'C1':'', 'C0':''} # 'C5':'', 'C6':'', 'C7':'', 'prop':''}
print(vectorC)

# Transforma la cadena de caracteres a binario
mensaje = ascii_bin(texto)[2:]

print(mensaje)

# Codificación
for i in mensaje:
    # prop = d(i) + C7
    #vectorC['prop'] = suma_xor(i, vectorC['C7'])

    # C7 = prop + C6
    #vectorC['C7'] = suma_xor(vectorC['prop'], vectorC['C6'])

    # C6 = C5
   # vectorC['C6'] = vectorC['C5']

    # C5 = prop + C4
    vectorC['prop'] = suma_xor(i, vectorC['C2'])

    # C2 = prop + C1
    vectorC['C2'] = vectorC['C1']

    # C1 = prop + C0
    vectorC['C1'] = vectorC['C0']

    # C0 = prop
    vectorC['C0'] = vectorC['prop']

r = "".join([b for b in vectorC.values()])
r= (r[:-1])
print(r)

print(mensaje,r)

#mensaje en ascii
bin_asciii = bin_ascii(mensaje)
print(bin_asciii)
