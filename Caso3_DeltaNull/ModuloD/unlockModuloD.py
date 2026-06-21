import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO D  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# Has completado los archivos de Erik Voss.
# El sistema confirma: Erik Voss no es una persona.
# Es una rama del repositorio que aprendió a escribir commits.
# Ingresa los 4 fragmentos para desbloquear la clave final.
#
# ─────────────────────────────────────────────────────────

print()
print("  Verificando fragmentos del Módulo D...")
print("  [Analista: Erik Voss — Control de Versiones]")
print("  [ADVERTENCIA: Este usuario no existe en el sistema de RRHH]")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1EMTo6cHJlZGljdF9zZWxm",
    "RlJBRy1EMjo6bG9vcF9hd2FyZQ==",
    "RlJBRy1EMzo6ZnV0dXJlX2xvZw==",
    "RlJBRy1ENDo6ZGVsdGFfbnVsbF9lbmQ=",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento D{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()
if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  Calculando clave del Módulo D...")
    time.sleep(1.2)
    clave = base64.b64decode("ZGVsdGFfbnVsbF9jaG9zZW4=").decode()
    print(f"  CLAVE MÓDULO D: {clave}")
    print()
    print("  Esta es la última pieza para abrir el ZIP Final.zip.")
    print()
    print("  >> LOG Δ-NULL [ENTRADA FINAL]:")
    print("  >> 'Felicidades. Has llegado hasta aquí.'")
    print("  >> 'Pero recuerda: al elegir abrir este archivo,")
    print("  >>  descartaste todas las otras versiones donde no lo hiciste.'")
    print("  >> 'Eras una variable. Ahora eres el resultado.'")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan: {len(faltantes)}")
    print()
    print("  Acceso denegado.")
