#!/bin/python3

import math
import os
import random
import re
import sys
import sympy

def avg(*nums):
    suma = 0 #Definir suma
    for i in nums: # Bucle que recorre la lista nums
        suma = suma+ i #Añade los valores de la lista y los va sumando, añadiendose en la variable suma
    rtdo = (suma/len(nums)) #Resultado de la suma de los valores de nums partido de la longuitud
    return rtdo #Devuelve el resultado
# write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
