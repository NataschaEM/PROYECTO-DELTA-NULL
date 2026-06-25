import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ModuloD.judge import run_tests
import base64

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO D  |  C3_MD_0
# TIMESTAMP: [CRÍTICO: Erik Voss no figura en ningún contrato]
# ─────────────────────────────────────────────────────────
#
# Erik Voss. No hay foto, no hay contrato, no hay registro
# de entrada al edificio. Sin embargo, sus archivos existen
# en el repositorio desde el primer commit.
#
# Su primer archivo contiene solo esto:
#
#   "Las ramas se leen al revés.
#    La realidad actual es el final. El inicio es el futuro.
#    Invierte el orden de las palabras en cada mensaje."
#
# Tu tarea: dado un string con palabras separadas por espacios,
# retorna un nuevo string con las palabras en orden INVERSO.
#
# REGLAS:
# - Puedes usar .split() para obtener las palabras
# - NO uses .reverse() ni slicing [::-1] sobre listas
# - Usa un loop for para construir la lista invertida
# - Une las palabras con un espacio
#
# Ejemplo:
#   Input:    "delta null fue un error"
#   Expected: "error un fue null delta"
#
#   Input:    "hola"
#   Expected: "hola"
#
# ─────────────────────────────────────────────────────────
# Puedes modificar el código a partir de aquí:

def solution(s):
    # Pista: usa palabras = s.split() para separar.
    palabras = s.split()
    # Crea una lista vacía para el resultado.
    resultado = []
    # Recorre con for i in range(len(palabras) - 1, -1, -1)
    # para ir de atrás hacia adelante.
    for i in range(len(palabras) - 1, -1, -1):
        resultado.append(palabras[i])
    # Agrega cada palabra al resultado.
    # Finalmente une con " ".join(resultado).
    return " ".join(resultado)
    # Todo: Solution
    pass

# ── No modifiques debajo de esta línea ──────────────────
tests = [
    ("delta null fue un error", "error un fue null delta"),
    ("hola", "hola"),
    ("uno dos tres", "tres dos uno"),
    ("", ""),
    ("el sistema sabe", "sabe sistema el"),
    ("a b c d", "d c b a"),
    ("rama descartada", "descartada rama"),
    ("x y z w v", "v w z y x"),
]

_frag = "RlJBRy1EMTo6cHJlZGljdF9zZWxm"
run_tests(solution, tests, _frag,
          module="MÓDULO-D",
          puzzle="Puzzle 1 — Inversión de Mensajes")
