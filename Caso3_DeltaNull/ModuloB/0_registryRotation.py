import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO B  |  C3_MB_0
# TIMESTAMP: [CONFLICTO: este archivo existe antes de ser creado]
# ─────────────────────────────────────────────────────────
#
# Marco Reyes era el encargado de la estructura de datos
# del sistema. En su carpeta se encontró una nota:
#
#   "El sistema rota los registros. Cada ciclo, el primer
#    elemento pasa al final. Así el sistema 'aprende' el orden.
#    Implementa una rotación hacia la izquierda de N posiciones."
#
# Tu tarea: dada una LISTA y un número entero n,
# retorna la lista rotada n posiciones hacia la IZQUIERDA.
# Rotar a la izquierda significa que el primer elemento
# se mueve al final.
#
# REGLAS:
# - El input es una TUPLA: (lista, n)
# - Retorna una lista (list)
# - Usa un loop for, NO uses slicing ni métodos de lista
# - Si la lista está vacía, retorna []
#
# Ejemplo:
#   Input:    ([1, 2, 3, 4, 5], 2)
#   Expected: [3, 4, 5, 1, 2]
#   (se mueven los primeros 2 al final)
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(entrada):
    lista, n = entrada
    # Pista: construye la nueva lista tomando primero los elementos
    # desde la posición n hasta el final, luego los primeros n.
    # Usa dos loops for con range().
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    (([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2]),
    (([10, 20, 30], 1), [20, 30, 10]),
    (([7, 8, 9], 3), [7, 8, 9]),
    (([], 2), []),
    (([1], 1), [1]),
    (([4, 5, 6, 7], 0), [4, 5, 6, 7]),
    (([1, 2, 3, 4, 5, 6], 3), [4, 5, 6, 1, 2, 3]),
    (([9, 0, 1], 2), [1, 9, 0]),
]

_frag = "RlJBRy1CMTo6cmVwb19naG9zdA=="
run_tests(solution, tests, _frag,
          module="MÓDULO-B",
          puzzle="Puzzle 1 — Rotación de Registros")
