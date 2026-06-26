import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO D  |  C3_MD_1
# TIMESTAMP: [CRÍTICO: Erik Voss no figura en ningún contrato]
# ─────────────────────────────────────────────────────────
#
# Segundo archivo de Erik. Encontrado en una carpeta llamada
# "/erikvoss_no_borrar" — creada por alguien más.
#
# Contenido del archivo:
#
#   "El ruido contamina la señal. Los símbolos y números
#    son artefactos de versiones incorrectas.
#    La señal pura solo contiene letras.
#    Purga todo lo que no sea alfabético."
#
# Tu tarea: dado un string s, retorna un nuevo string
# que contiene SOLO las letras del alfabeto (a-z, A-Z).
# Elimina números, espacios, símbolos, guiones, etc.
#
# REGLAS:
# - Usa un loop for
# - Define las letras válidas como un string: "abcde...xyzABC...XYZ"
# - NO uses .isalpha() ni métodos similares
#
# Ejemplo:
#   Input:    "d3lt4_null_v2!"
#   Expected: "dltnullv"
#
#   Input:    "123!@#"
#   Expected: ""
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: define letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Crea resultado = ""
    resultado = ""
    # Recorre s con for. Si el carácter está en letras, agrégalo al resultado.
    for caracter in s:
        if caracter in letras:
            resultado+=caracter
    
    return resultado
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("d3lt4_null_v2!", "dltnullv"),
    ("123!@#", ""),
    ("hello world", "helloworld"),
    ("Δ-Null-2031", "Null"),
    ("abc", "abc"),
    ("", ""),
    ("A1B2C3", "ABC"),
    ("Erik Voss :: 0000", "ErikVoss"),
]

_frag = "RlJBRy1EMjo6bG9vcF9hd2FyZQ=="
run_tests(solution, tests, _frag,
          module="MÓDULO-D",
          puzzle="Puzzle 2 — Purga de Señal")
