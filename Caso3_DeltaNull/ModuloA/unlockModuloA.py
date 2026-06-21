import sys
import os
import base64
import time

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  MÓDULO A  |  UNLOCK
# Ejecuta este script SOLO cuando tengas los 4 fragmentos.
# ─────────────────────────────────────────────────────────
#
# Has completado los registros de Vera Solano.
# Sus archivos fueron los primeros en ser "versionados".
# Ingresa los 4 fragmentos para desbloquear la clave del módulo.
#
# ─────────────────────────────────────────────────────────

print()
print("  Verificando fragmentos del Módulo A...")
print("  [Analista: Vera Solano — Ingeniería de Sistemas]")
print()
time.sleep(1)

FRAGMENTOS_VALIDOS = {
    "RlJBRy1BMTo6ZGVsdGFfaW5pdA==",
    "RlJBRy1BMjo6dmVyc2lvbl96ZXJv",
    "RlJBRy1BMzo6bnVsbF9icmFuY2g=",
    "RlJBRy1BNDo6dGltZXN0YW1wX3ZvaWQ=",
}

ingresados = set()
for i in range(1, 5):
    frag = input(f"  Fragmento A{i}: ").strip()
    frag_encoded = base64.b64encode(frag.encode()).decode()
    ingresados.add(frag_encoded)

print()
if ingresados == FRAGMENTOS_VALIDOS:
    time.sleep(0.8)
    print("  Todos los fragmentos verificados.")
    time.sleep(1)
    print()
    print("  Calculando clave del Módulo A...")
    time.sleep(1.2)
    clave = base64.b64decode("cmVhbGl0eV9mb3JrZWQ=").decode()
    print(f"  CLAVE MÓDULO A: {clave}")
    print()
    print("  Esta es una pieza para abrir el ZIP Final.zip.")
    print()
    print("  >> LOG Δ-NULL: 'La rama de Vera fue la primera en divergir.'")
    print("  >> ADVERTENCIA: Sus commits tienen timestamps del año 2031.")
    print()
else:
    faltantes = FRAGMENTOS_VALIDOS - ingresados
    print(f"  Fragmentos incorrectos o incompletos.")
    print(f"  Faltan: {len(faltantes)}")
    print()
    print("  Acceso denegado.")
