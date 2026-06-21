import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloB.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO B  |  C3_MB_1
# TIMESTAMP: [CONFLICTO: este archivo existe antes de ser creado]
# ─────────────────────────────────────────────────────────
#
# Marco dejó este mensaje en el repositorio:
#
#   "Los identificadores de rama deben ser SOLO numéricos.
#    Cualquier carácter no-numérico indica que la rama
#    fue manipulada externamente. Necesito un validador."
#
# Tu tarea: dado un string s, retorna True si TODOS sus
# caracteres son dígitos (0-9), o False si alguno no lo es.
# Un string vacío retorna False.
#
# REGLAS:
# - Usa un loop for para revisar cada carácter
# - NO uses el método .isdigit() ni .isnumeric()
# - Compara usando los caracteres "0" al "9"
# - String vacío → False
#
# Ejemplo:
#   Input:    "20241107"
#   Expected: True
#
#   Input:    "2024-11-07"
#   Expected: False  (el guión no es dígito)
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: define una lista o string con los dígitos válidos: "0123456789"
    # Recorre s con for. Si algún char no está en los dígitos, retorna False.
    # Al final del loop retorna True.
    # Recuerda manejar el caso del string vacío primero.
    # Todo: Solution
    # Definir el string con los dígitos válidos.
    digitos = "0123456789"
    # Caso con el string vacio.
    if s == "":
     return False
    # recorrer s con un for y asignar True o False al input.
    for i in range(len(s)):
        if s[i] not in digitos:
            return False
    return True
        
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("20241107", True),
    ("2024-11-07", False),
    ("", False),
    ("0", True),
    ("000000", True),
    ("abc", False),
    ("123abc", False),
    ("9999999999", True),
    (" 123", False),
    ("12 34", False),
]

_frag = "RlJBRy1CMjo6ZWNob19sb29w"
run_tests(solution, tests, _frag,
          module="MÓDULO-B",
          puzzle="Puzzle 2 — Validador de Identificadores")
