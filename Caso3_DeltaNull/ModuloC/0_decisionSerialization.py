import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO C  |  C3_MC_0
# TIMESTAMP: [PARADOJA: archivo modificado 3 días antes de su creación]
# ─────────────────────────────────────────────────────────
#
# Sofia Ibáñez era la arquitecta del motor de predicción.
# Sus archivos son los más perturbadores del repositorio.
#
# Una nota encontrada en su carpeta:
#
#   "Δ-Null convierte decisiones en números.
#    Para transmitirlas entre módulos, los números deben
#    serialzarse como texto. Necesito convertir una lista
#    de enteros en una lista de sus representaciones
#    como string."
#
# Tu tarea: dada una lista de enteros, retorna una nueva lista
# donde cada número ha sido convertido a string.
#
# REGLAS:
# - Usa un loop for
# - Usa str() para convertir cada número
# - NO uses map() ni comprensiones de lista
# - Retorna una lista nueva
#
# Ejemplo:
#   Input:    [1, 2, 3]
#   Expected: ["1", "2", "3"]
#
#   Input:    [0, -5, 100]
#   Expected: ["0", "-5", "100"]
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista):
    resultado = [ ] #Se crea una lista vacía en donde se añadirán los elementos transformados a strings
    for numero in lista: #Este ciclo sirve para pasar por cada uno de los elementos de la lista, en este caso, los números
        resultado.append(str(numero)) #Por cada número, se usa el .append(), el cual, permite agregar elementos a una lista
        #En este caso, se agregan los elementos nuevos en la lista vacía creada anteriormente, y en la lista, se añaden los números transformados a strings
    print(resultado) #Se imprime la lista del resultado, que muestra los números ya transformados a strings
    return resultado #La función devuelve la lista resultado.
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ([1, 2, 3], ["1", "2", "3"]),
    ([0, -5, 100], ["0", "-5", "100"]),
    ([], []),
    ([42], ["42"]),
    ([10, 20, 30, 40], ["10", "20", "30", "40"]),
    ([-1, -2, -3], ["-1", "-2", "-3"]),
    ([0, 0, 0], ["0", "0", "0"]),
    ([999, 1000], ["999", "1000"]),
]

_frag = "RlJBRy1DMTo6bWVyZ2VfZmFpbA=="
run_tests(solution, tests, _frag,
          module="MÓDULO-C",
          puzzle="Puzzle 1 — Serialización de Decisiones")
