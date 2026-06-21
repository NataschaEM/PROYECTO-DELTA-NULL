import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO C  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# Has reconstruido los archivos de Sofia Ibáñez.
# Sus predicciones describen eventos que aún no han ocurrido.
# Ingresa los 4 fragmentos para desbloquear la clave del módulo.
#
# ─────────────────────────────────────────────────────────

print()
print("  Verificando fragmentos del Módulo C...")
print("  [Analista: Sofia Ibáñez — Sistemas de Predicción]")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1DMTo6bWVyZ2VfZmFpbA==",
    "RlJBRy1DMjo6YnJhbmNoX2xvc3Q=",
    "RlJBRy1DMzo6aXRlcl9zZXZlbg==",
    "RlJBRy1DNDo6cGhhbnRvbV9kaWZm",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento C{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()
if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  Calculando clave del Módulo C...")
    time.sleep(1.2)
    clave = base64.b64decode("YnJhbmNoX3NlbGVjdGVk").decode()
    print(f"  CLAVE MÓDULO C: {clave}")
    print()
    print("  Esta es una pieza para abrir el ZIP Final.zip.")
    print()
    print("  >> LOG Δ-NULL: 'Sofia fue la última en comprenderlo.'")
    print("  >> 'No somos los investigadores. Somos las variables.'")
    print("  >> Archivo de Sofia — última modificación: [FECHA INVÁLIDA]")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan: {len(faltantes)}")
    print()
    print("  Acceso denegado.")
