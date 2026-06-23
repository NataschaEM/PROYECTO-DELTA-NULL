import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloC.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO C  |  C3_MC_2
# TIMESTAMP: [PARADOJA: archivo modificado 3 días antes de su creación]
# ─────────────────────────────────────────────────────────
#
# Sofia dejó un reporte técnico parcialmente borrado:
#
#   "Δ-Null codifica el nivel de 'certeza' de una predicción
#    usando letras MAYÚSCULAS en los identificadores.
#    Más mayúsculas = mayor certeza del sistema sobre esa rama.
#    El analizador cuenta cuántas letras mayúsculas hay
#    en cada identificador de versión."
#
# Tu tarea: dado un string s, retorna cuántas letras
# mayúsculas contiene (A-Z).
#
# REGLAS:
# - Usa un loop for
# - NO uses .isupper() ni métodos similares
# - Compara usando los caracteres "A" hasta "Z"
# - Solo cuentan letras del alfabeto inglés (A-Z)
# - Los números, espacios y símbolos NO cuentan
#
# Ejemplo:
#   Input:    "DeltaNullV2"
#   Expected: 3   (D, N, V)
#
#   Input:    "todo_minusculas"
#   Expected: 0
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    mayúsculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    contador = 0
    for LETRA in s:
        if LETRA in mayúsculas:
            contador = contador + 1
    return contador

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("DeltaNullV2", 3),
    ("todo_minusculas", 0),
    ("", 0),
    ("ABC", 3),
    ("abc123ABC", 3),
    ("Delta-Null-CORE", 6),
    ("A", 1),
    ("123!@#", 0),
    ("MiXeD cAsE", 5),
]

_frag = "RlJBRy1DMzo6aXRlcl9zZXZlbg=="
run_tests(solution, tests, _frag,
          module="MÓDULO-C",
          puzzle="Puzzle 3 — Nivel de Certeza")
