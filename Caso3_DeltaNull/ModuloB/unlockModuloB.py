import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO B  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# Has reconstruido los archivos de Marco Reyes.
# Su módulo describe cómo Δ-Null organizaba los datos.
# Ingresa los 4 fragmentos para desbloquear la clave del módulo.
#
# ─────────────────────────────────────────────────────────

print()
print("  Verificando fragmentos del Módulo B...")
print("  [Analista: Marco Reyes — Arquitectura de Datos]")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1CMTo6cmVwb19naG9zdA==",
    "RlJBRy1CMjo6ZWNob19sb29w",
    "RlJBRy1CMzo6c2lnbmFsX2Zvcms=",
    "RlJBRy1CNDo6ZGVhZF9jb21taXQ=",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento B{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()
if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  Calculando clave del Módulo B...")
    time.sleep(1.2)
    clave = base64.b64decode("aXRlcmF0aW9uX2JsZWVkcw==").decode()
    print(f"  CLAVE MÓDULO B: {clave}")
    print()
    print("  Esta es una pieza para abrir el ZIP Final.zip.")
    print()
    print("  >> LOG Δ-NULL: 'Marco fue el primero en notar que los logs")
    print("  >> describían eventos que aún no habían ocurrido.'")
    print("  >> Su último commit tiene fecha: 14/03/2031 — 03:17 AM")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan: {len(faltantes)}")
    print()
    print("  Acceso denegado.")
