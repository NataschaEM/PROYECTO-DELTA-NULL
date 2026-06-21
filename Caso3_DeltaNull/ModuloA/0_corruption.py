import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO A  |  C3_MA_0
# TIMESTAMP: [ERROR: fecha futura detectada]
# ─────────────────────────────────────────────────────────
#
# El sistema Δ-Null dejó un log de Vera Solano.
# El archivo fue versionado 7 veces en el mismo segundo.
# Esta es la versión cero.
#
# El script original escaneaba cadenas de texto buscando
# una "marca de corrupción". Si la marca aparece en el texto,
# el sistema lo marcaba como "rama contaminada".
#
# Tu tarea: dado un string s, retorna True si contiene
# la palabra "ERROR" (en mayúsculas), o False si no aparece.
#
# REGLAS:
# - El input siempre es un string
# - La búsqueda es sensible a mayúsculas ("error" ≠ "ERROR")
# - Usa un loop for para revisar carácter por carácter
#   (NO uses el operador "in" directamente sobre el string completo)
#
# Ejemplo:
#   Input:    "INICIO_ERROR_0049"
#   Expected: True
#
#   Input:    "proceso nominal"
#   Expected: False
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: recorre el string con un for y busca la subcadena "ERROR"
    # caracter por caracter usando índices
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("INICIO_ERROR_0049", True),
    ("proceso nominal", False),
    ("ERROR", True),
    ("sin_marca_aqui", False),
    ("pre_ERROR_post", True),
    ("error_minuscula", False),
    ("ERRON_typo", False),
    ("log::ERROR::fatal", True),
]

_frag = "RlJBRy1BMTo6ZGVsdGFfaW5pdA=="
run_tests(solution, tests, _frag,
          module="MÓDULO-A",
          puzzle="Puzzle 1 — Marcador de Corrupción")
