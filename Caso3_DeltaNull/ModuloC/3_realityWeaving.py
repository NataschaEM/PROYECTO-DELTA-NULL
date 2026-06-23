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
    s1, s2 = entrada
    if len(s1) > len(s2):
        minimo = len(s2)
        no_minimo = s1
    else:
        minimo = len(s1)
        no_minimo = s2

    resultado = ""
    for posicion_string in range(minimo):
        resultado = resultado + (s1[posicion_string] + s2[posicion_string])
    resultado = f"{resultado}{no_minimo[minimo: ]}"
    return resultado

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
