import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO B  |  C3_MB_2
# TIMESTAMP: [CONFLICTO: este archivo existe antes de ser creado]
# ─────────────────────────────────────────────────────────
#
# Una bitácora de Marco dice:
#
#   "Δ-Null almacena los datos en capas anidadas.
#    Para comparar versiones necesito aplanar la estructura:
#    convertir una lista de listas en una sola lista plana,
#    manteniendo el orden original de los elementos."
#
# Tu tarea: dada una LISTA DE LISTAS, retorna una sola lista
# con todos los elementos en orden.
#
# REGLAS:
# - El input siempre es una lista de listas (pueden estar vacías)
# - Usa dos loops for anidados
# - NO uses extend() ni sum() con listas
# - Mantén el orden original
#
# Ejemplo:
#   Input:    [[1, 2], [3, 4], [5]]
#   Expected: [1, 2, 3, 4, 5]
#
#   Input:    [[], [1], [], [2, 3]]
#   Expected: [1, 2, 3]
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista_de_listas):
    # Pista: crea una lista resultado vacía.
    # Con el primer for recorre cada sublista.
    # Con el segundo for recorre cada elemento de esa sublista.
    # Agrega cada elemento al resultado.
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ([[1, 2], [3, 4], [5]], [1, 2, 3, 4, 5]),
    ([[], [1], [], [2, 3]], [1, 2, 3]),
    ([], []),
    ([[10]], [10]),
    ([["a", "b"], ["c"]], ["a", "b", "c"]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([[], [], []], []),
    ([[True, False], [True]], [True, False, True]),
]

_frag = "RlJBRy1CMzo6c2lnbmFsX2Zvcms="
run_tests(solution, tests, _frag,
          module="MÓDULO-B",
          puzzle="Puzzle 3 — Aplanado de Capas")
