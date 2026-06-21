import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO D  |  C3_MD_3
# TIMESTAMP: [CRÍTICO: Erik Voss no figura en ningún contrato]
# ─────────────────────────────────────────────────────────
#
# El último archivo de Erik. Contiene un solo comentario
# antes del código:
#
#   "Δ-Null no predice el futuro.
#    Δ-Null crea un espejo de sí mismo.
#    El sistema tomó cada identificador de versión y le
#    concatenó su propio reverso, creando una 'firma espejo'.
#    Esto era la firma de identidad de cada rama."
#
# Tu tarea: dado un string s, retorna el string original
# seguido de su reverso.
#
# REGLAS:
# - Usa un loop for para construir el reverso
# - NO uses [::-1] ni .reverse()
# - Concatena el string original con el reverso generado
#
# Ejemplo:
#   Input:    "delta"
#   Expected: "deltaatle d"
#   ESPERA — incorrecto. La firma es:
#   "delta" + reverso de "delta" = "delta" + "atled" = "deltaatled"
#
#   Input:    "AB"
#   Expected: "ABBA"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: construye el reverso con un loop.
    # Recorre s con for i in range(len(s) - 1, -1, -1)
    # y concatena cada carácter.
    # Retorna s + reverso.
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("delta", "deltaatled"),
    ("AB", "ABBA"),
    ("", ""),
    ("a", "aa"),
    ("null", "nullllun"),
    ("erik", "erikkire"),
    ("XY", "XYYX"),
    ("abc", "abccba"),
]

_frag = "RlJBRy1ENDo6ZGVsdGFfbnVsbF9lbmQ="
run_tests(solution, tests, _frag,
          module="MÓDULO-D",
          puzzle="Puzzle 4 — Firma Espejo")
