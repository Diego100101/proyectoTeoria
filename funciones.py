# función para suma binaria
import sys


def suma_xor(a, b):
    if a == b:
        return '0'
    else:
        return '1'

def ascii_bin(texto):
    mensaje = texto.encode()
    binario = int.from_bytes(mensaje, "big")
    return bin(binario)

def verificaLlave(llave):
    if len(llave) != 3:
        print("El tamaño de la llave debe ser de 8 bits")
        sys.exit()
    for b in llave:
        if b != '0':
            if b != '1':
                print("Solo ingresa bits")
                sys.exit()

def verificaTexto(texto):
    if len(texto) > 32:
        print()
        sys.exit()

def bin_ascii(binario):
    texto = ""
    for b in range(0,len(binario),8):
        ini,fin = b, b+8
        bina = binario [ini:fin]
        valor = int(bina,2)
        texto += chr(valor)
    return texto
