import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO C  |  C3_MC_1
# TIMESTAMP: [PARADOJA: archivo modificado 3 días antes de su creación]
# ─────────────────────────────────────────────────────────
#
# En el diario de Sofia hay esta entrada:
#
#   "[Entrada sin fecha]
#    El sistema necesita identificar el 'pico de predicción':
#    el valor máximo en una secuencia de datos.
#    Esto determina qué rama tiene más probabilidad de
#    convertirse en la realidad dominante.
#    El motor no puede usar funciones nativas de Python
#    para esto — debe calcularlo desde cero."
#
# Tu tarea: dada una lista de números enteros (siempre
# tendrá al menos un elemento), retorna el valor máximo.
#
# REGLAS:
# - NO uses max() ni sorted()
# - Usa un loop for con una variable auxiliar
# - El primer elemento de la lista puede ser tu valor inicial
#
# Ejemplo:
#   Input:    [3, 7, 2, 9, 1]
#   Expected: 9
#
#   Input:    [-5, -1, -10]
#   Expected: -1
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ([3, 7, 2, 9, 1], 9),
    ([-5, -1, -10], -1),
    ([42], 42),
    ([1, 1, 1, 1], 1),
    ([100, 0, 50], 100),
    ([0, 0, 1], 1),
    ([5, 4, 3, 2, 1], 5),
    ([1, 2, 3, 4, 5], 5),
]

_frag = "RlJBRy1DMjo6YnJhbmNoX2xvc3Q="
run_tests(solution, tests, _frag,
          module="MÓDULO-C",
          puzzle="Puzzle 2 — Pico de Predicción")
