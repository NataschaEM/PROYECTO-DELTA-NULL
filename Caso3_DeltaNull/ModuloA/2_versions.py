import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO A  |  C3_MA_2
# TIMESTAMP: [ERROR: fecha futura detectada]
# ─────────────────────────────────────────────────────────
#
# En una bitácora de Vera se encontró este fragmento:
#
#   "El sistema genera versiones. Algunas son válidas,
#    otras son ramas muertas. Necesito contar cuántas
#    versiones tienen longitud exactamente igual a 8.
#    Esos son los registros activos."
#
# Tu tarea: dada una LISTA de strings, retorna cuántos
# de esos strings tienen exactamente 8 caracteres de longitud.
#
# REGLAS:
# - El input es una lista de strings
# - Retorna un número entero (int)
# - Usa un loop for y un contador
# - Usa len() para medir la longitud
#
# Ejemplo:
#   Input:    ["version1", "v2", "branch00", "null"]
#   Expected: 2
#   ("version1" tiene 8 chars, "branch00" tiene 8 chars)
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(lista):
    # Pista: inicializa un contador en 0.
    # Recorre la lista con for y suma 1 cuando len(item) == 8.
    # Todo: Solution
    #El contador va a iniciar en 0
    contador = 0
    #el for va a recorrer cada item de la lista
    for i in lista:
        #el if va a verificar que cumpla con la longitud de 8
        if len(i) == 8:
            #si cumple, se le suma 1 en el contador 
            contador += 1
    return contador
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    (["version1", "v2", "branch00", "null"], 2),
    (["abcdefgh", "abc", "12345678", "xyz"], 2),
    ([], 0),
    (["delta000", "delta001", "delta002"], 3),
    (["a", "ab", "abc", "abcd"], 0),
    (["null_end", "ok"], 1),
    (["12345678", "87654321", "x"], 2),
    (["00000000"], 1),
]

_frag = "RlJBRy1BMzo6bnVsbF9icmFuY2g="
run_tests(solution, tests, _frag,
          module="MÓDULO-A",
          puzzle="Puzzle 3 — Auditoría de Versiones")
