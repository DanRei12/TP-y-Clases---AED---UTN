import random
letras = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

class Transaccion:
    def __init__(self, opcode, numcuenta, importe, caja_num):
        self.opcode = opcode
        self.numcuenta = numcuenta
        self.importe = importe
        self.caja_num = caja_num

def automatic_charge(n):
    vec = []
    for i in range(n):
        opcode = random.randrange(1, 21)
        numcuenta = random.randrange(10)
        importe = random.randrange(1, 9999)
        caja_num = random.randrange(10)
        trans = Transaccion(opcode, numcuenta, importe, caja_num)
        vec.append(trans)
    return vec


def val_range(desde, hasta, mensaje):
    num = int(input(mensaje))
    while num <= desde or num >= hasta:
        print('Valor no válido. Ingrese un valor entre', desde, 'y', hasta)
        num = int(input(mensaje))
    return num
