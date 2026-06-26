import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO D  |  C3_MD_2
# TIMESTAMP: [CRÍTICO: Erik Voss no figura en ningún contrato]
# ─────────────────────────────────────────────────────────
#
# Tercer archivo de Erik. Este fue encontrado abierto,
# como si alguien lo estuviera editando en este momento.
#
#   "[Nota al margen, escrita a mano según el metadato]
#    El orden importa. Una realidad coherente tiene sus
#    eventos en secuencia. Si la lista está desordenada,
#    la rama es inválida y debe ser descartada.
#    Verifica si una secuencia está ordenada de menor a mayor."
#
# Tu tarea: dada una lista de números, retorna True si
# está ordenada de MENOR a MAYOR (ascendente), o False si no.
# Una lista vacía o con un solo elemento retorna True.
#
# REGLAS:
# - Usa un loop for con índices
# - NO uses sorted() ni .sort()
# - Compara cada elemento con el siguiente
#
# Ejemplo:
#   Input:    [1, 2, 3, 4, 5]
#   Expected: True
#
#   Input:    [1, 3, 2, 5]
#   Expected: False
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista):
    
    # Pista: recorre la lista con for i in range(len(lista) - 1).
    # Compara lista[i] con lista[i+1].
    # Si lista[i] > lista[i+1], retorna False inmediatamente.
    for i in range(len(lista) -1):
        if lista[i] > lista[i+1]:
            return False
    return True

    # Si el loop termina sin problemas, retorna True.
    
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ([1, 2, 3, 4, 5], True),
    ([1, 3, 2, 5], False),
    ([], True),
    ([7], True),
    ([1, 1, 1], True),
    ([5, 4, 3, 2, 1], False),
    ([0, 10, 20, 30], True),
    ([1, 2, 3, 3, 4], True),
    ([100, 50], False),
]

_frag = "RlJBRy1EMzo6ZnV0dXJlX2xvZw=="
run_tests(solution, tests, _frag,
          module="MÓDULO-D",
          puzzle="Puzzle 3 — Verificación de Secuencia")
