import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO A  |  C3_MA_3
# TIMESTAMP: [ERROR: fecha futura detectada]
# ─────────────────────────────────────────────────────────
#
# El último archivo de Vera contiene una nota críptica:
#
#   "Cada rama debe ser sellada. El sello consiste en
#    tomar los primeros 4 caracteres del identificador
#    y añadir el sufijo '::SEALED' al final.
#    Si el identificador tiene menos de 4 caracteres,
#    se usa completo."
#
# Tu tarea: dado un string s, retorna los primeros 4
# caracteres (o todos si hay menos de 4) seguidos de "::SEALED".
#
# REGLAS:
# - Usa un loop for y construye el resultado carácter por carácter
#   (NO uses slicing directo como s[:4])
# - El sufijo siempre es "::SEALED"
# - Si el string tiene 0 caracteres, retorna "::SEALED"
#
# Ejemplo:
#   Input:    "delta_null_core"
#   Expected: "delt::SEALED"
#
#   Input:    "ab"
#   Expected: "ab::SEALED"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: usa un for con range y una variable contador.
    # Detén el loop cuando hayas tomado 4 caracteres.
    # Luego concatena "::SEALED".
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("delta_null_core", "delt::SEALED"),
    ("ab", "ab::SEALED"),
    ("", "::SEALED"),
    ("xyz!", "xyz!::SEALED"),
    ("vera_solano_log", "vera::SEALED"),
    ("abc", "abc::SEALED"),
    ("ABCD1234", "ABCD::SEALED"),
    ("X", "X::SEALED"),
]

_frag = "RlJBRy1BNDo6dGltZXN0YW1wX3ZvaWQ="
run_tests(solution, tests, _frag,
          module="MÓDULO-A",
          puzzle="Puzzle 4 — Sello de Rama")
