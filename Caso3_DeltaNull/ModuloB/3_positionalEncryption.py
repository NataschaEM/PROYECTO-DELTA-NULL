import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO B  |  C3_MB_3
# TIMESTAMP: [CONFLICTO: este archivo existe antes de ser creado]
# ─────────────────────────────────────────────────────────
#
# El último log de Marco contiene esto:
#
#   "Para ofuscar los datos entre versiones, Δ-Null
#    usaba un esquema simple: tomar cada carácter del
#    texto y registrarlo como su POSICIÓN seguida del carácter.
#    Así 'abc' se convierte en '0a1b2c'.
#    El sistema usa esto para detectar si un archivo fue
#    alterado entre ramas."
#
# Tu tarea: dado un string s, retorna un nuevo string
# donde cada carácter va precedido por su índice (posición).
#
# REGLAS:
# - Usa un loop for con range(len(s))
# - Concatena el índice (como string) + el carácter
# - El string vacío retorna ""
#
# Ejemplo:
#   Input:    "abc"
#   Expected: "0a1b2c"
#
#   Input:    "hi"
#   Expected: "0h1i"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: crea un resultado vacío.
    # Usa for i in range(len(s)):
    # En cada iteración agrega str(i) + s[i] al resultado.
    # Todo: Solution
    # Resultado vacío.
    resultado = ""
    # for in range
    for i in range(len(s)):
        resultado = resultado + str(i) + s[i]
    # Ingresar el resultado
    return resultado
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("abc", "0a1b2c"),
    ("hi", "0h1i"),
    ("", ""),
    ("x", "0x"),
    ("delta", "0d1e2l3t4a"),
    ("null", "0n1u2l3l"),
    ("123", "011223"),
    ("AB", "0A1B"),
]

_frag = "RlJBRy1CNDo6ZGVhZF9jb21taXQ="
run_tests(solution, tests, _frag,
          module="MÓDULO-B",
          puzzle="Puzzle 4 — Codificación Posicional")
