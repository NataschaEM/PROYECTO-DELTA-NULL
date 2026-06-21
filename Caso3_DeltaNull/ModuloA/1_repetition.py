import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloA.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO A  |  C3_MA_1
# TIMESTAMP: [ERROR: fecha futura detectada]
# ─────────────────────────────────────────────────────────
#
# Vera encontró algo extraño: el sistema repetía caracteres
# de forma consecutiva en ciertos logs, como si hubiera
# sufrido un "tartamudeo" al escribir.
#
# Ejemplo del log original:
#   "sssiissteema  ccoorruuppttoo"
#
# El script de limpieza debía eliminar los caracteres
# CONSECUTIVOS duplicados, dejando solo una aparición
# de cada carácter cuando se repite seguido.
#
# Tu tarea: dado un string s, retorna un nuevo string
# sin caracteres consecutivos repetidos.
#
# REGLAS:
# - Solo eliminar duplicados CONSECUTIVOS (no todos los duplicados)
# - "aab" → "ab"   pero   "aba" → "aba" (la 'a' no es consecutiva)
# - El string puede tener espacios y números
# - Usa un loop for
#
# Ejemplo:
#   Input:    "sssiissteema"
#   Expected: "sistema"
#
#   Input:    "hola"
#   Expected: "hola"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: construye un string resultado.
    # Agrega el carácter actual solo si es diferente al anterior.
    # Todo: Solution
    #Va ir guardando el string sin repetir los caracteres
    resultado = ""
    #Va ir guardando el ultimo caracteres que se uso para validar que no se repita
    ultimo_char = ""
    #El for va a ir recorriendo caracter por caracter 
    for char in s:
        #El if va a validar que el ultimo caracter sea diferente al siguiente en revisión
        #si son iguales no hara nada, si es diferente va a entrar a la condicion
         if char != ultimo_char:
             resultado += char
             ultimo_char = char
    return resultado
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("sssiissteema", "sistema"),
    ("hola", "hola"),
    ("aabbcc", "abc"),
    ("aaaa", "a"),
    ("abcde", "abcde"),
    ("  espacios  ", " espacios "),
    ("11223344", "1234"),
    ("delta__null", "delta_nul"),
]

_frag = "RlJBRy1BMjo6dmVyc2lvbl96ZXJv"
run_tests(solution, tests, _frag,
          module="MÓDULO-A",
          puzzle="Puzzle 2 — Limpieza de Repeticiones")
