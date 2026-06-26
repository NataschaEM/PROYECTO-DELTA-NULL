import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO C  |  C3_MC_3
# TIMESTAMP: [PARADOJA: archivo modificado 3 días antes de su creación]
# ─────────────────────────────────────────────────────────
#
# El archivo más perturbador de Sofia:
#
#   "Δ-Null 'teje' dos versiones de la realidad en una sola.
#    Toma dos strings y los entrelaza: un carácter de A,
#    uno de B, uno de A, uno de B...
#    Si uno es más largo, agrega el resto al final.
#    Así nace una 'rama híbrida'."
#
# Tu tarea: dada una TUPLA de dos strings (s1, s2),
# retorna un string con los caracteres entrelazados.
# Si uno es más largo, sus caracteres restantes se agregan al final.
#
# REGLAS:
# - El input es una tupla: (s1, s2)
# - Usa un loop for con range
# - NO uses zip() ni métodos avanzados
#
# Ejemplo:
#   Input:    ("abc", "12345")
#   Expected: "a1b2c345"
#
#   Input:    ("hola", "")
#   Expected: "hola"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(entrada):
    s1, s2 = entrada #Estas son las entradas, que es la tupla de los dos strings dados
    if len(s1) > len(s2): #Se comparan las longitudes de ambos strings, esto para averiguar cual es mayor
        minimo = len(s2) #Si la longitud del primer string resulta mayor, se guarda el otro string como el más pequeño
        no_minimo = s1 #El otro string que es más largo queda guardado en otra variable que indica que es el más largo
    else:
        minimo = len(s1) #Si la longitud del segundo string resulta igual o mayor, se guarda el primer string como el más pequeño
        no_minimo = s2 #Y el string dos queda guardado como el string más largo

    resultado = "" #Se guarda una variable con un string vacío, en donde colocaremos nuestro string intercalado
    for posicion_string in range(minimo): #Se abre un ciclo que ocurrirá la cantidad de veces que sea igual a la longitud del string minimo
        resultado = resultado + (s1[posicion_string] + s2[posicion_string]) #Cada vez que pase el ciclo, se le suma al resultado la posición del string en el que estén de ambos strings
    #Por ejemplo, si van por el número 0, se colocará el caracter en la posición número 0 de ambos strings, se suman, y se agregan a la variable de resultado
    resultado = f"{resultado}{no_minimo[minimo: ]}" #Al final del ciclo, el resultado queda un string que suma el resultado del ciclo y el resto del string que era más largo
    return resultado #Se devuelve la variable resultado con los arreglos hechos al final del ciclo.

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    (("abc", "12345"), "a1b2c345"),
    (("hola", ""), "hola"),
    (("", "xyz"), "xyz"),
    (("ab", "cd"), "acbd"),
    (("A", "B"), "AB"),
    (("delta", "NULL0"), "dNeUlLtLa0"),
    (("", ""), ""),
    (("xx", "yyy"), "xyxyy"),
]

_frag = "RlJBRy1DNDo6cGhhbnRvbV9kaWZm"
run_tests(solution, tests, _frag,
          module="MÓDULO-C",
          puzzle="Puzzle 4 — Tejido de Realidades")
