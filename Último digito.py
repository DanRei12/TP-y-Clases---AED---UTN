'''Programa para poder determinar la última cifra y las dos últimas de un número en específico.'''
__author__ = 'Danielin :D'
print ("Este programa permitira que visualice la última cifra de un número y las dos últimas cifras de un número.""\n")
a = int(input("Ingrese un valor númerico entero con 3 cifras o más: "))
ultdig = a%10
ultdig2 = a%100
print ("El último dígito es:", ultdig, "\n""Los últimos dos dígitos son:", ultdig2)
print (input())
