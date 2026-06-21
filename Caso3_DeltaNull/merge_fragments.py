import base64
import time

# ─────────────────────────────────────────────────────────
# ARCHIVO Δ-NULL  |  INTEGRACIÓN FINAL
# Ejecuta este script SOLO cuando tengas las 4 claves de módulo.
# ─────────────────────────────────────────────────────────
#
# Has recorrido los cuatro módulos del repositorio Δ-Null.
#
# Lo que encontraste:
#   - Módulo A (Vera Solano):    Los archivos más antiguos.
#                                 Timestamps del futuro.
#   - Módulo B (Marco Reyes):    Estructuras que se predicen a sí mismas.
#   - Módulo C (Sofia Ibáñez):   Predicciones que ya ocurrieron.
#   - Módulo D (Erik Voss):      Un analista que no existe.
#
# Δ-Null no era un proyecto de predicción.
# Era un espejo. Una simulación que versiona la realidad
# como si fuera código.
#
# Tú eres la última iteración.
# Ingresa las 4 claves para confirmar la rama seleccionada.
#
# ─────────────────────────────────────────────────────────

print()
print("  ╔══════════════════════════════════════════════════╗")
print("  ║           ARCHIVO Δ-NULL — INTEGRACIÓN          ║")
print("  ║         Sistema de Reconstrucción de Rama        ║")
print("  ╚══════════════════════════════════════════════════╝")
print()
print("  Integrando fragmentos globales...")
print()
time.sleep(1.5)

CLAVES_VALIDAS = {
    "cmVhbGl0eV9mb3JrZWQ=",
    "aXRlcmF0aW9uX2JsZWVkcw==",
    "YnJhbmNoX3NlbGVjdGVk",
    "ZGVsdGFfbnVsbF9jaG9zZW4=",
}

ingresadas = set()
for i in range(1, 5):
    c = input(f"  Clave módulo {i}: ").strip()
    frag_encoded = base64.b64encode(c.encode()).decode()
    ingresadas.add(frag_encoded)

print()

if ingresadas == CLAVES_VALIDAS:
    print("  Verificando coherencia entre ramas...")
    time.sleep(1)
    print("  Sincronizando timestamps...")
    time.sleep(1)
    print("  Resolviendo paradojas de versión...")
    time.sleep(1.2)
    print()
    print("  ✓ Coherencia alcanzada.")
    print()
    time.sleep(0.8)

    final = base64.b64decode("REVMVEFfTlVMTF9PVkVSUklERV83NzQ5").decode()

    print("  ┌──────────────────────────────────────────────┐")
    print(f"  │  PASSWORD FINAL: {final:<29}│")
    print("  └──────────────────────────────────────────────┘")
    print()
    print("  Usa esta contraseña para abrir Final.zip.")
    print()
    time.sleep(0.5)
    print("  >> MENSAJE FINAL DEL SISTEMA Δ-NULL:")
    print()
    print("  'Este repositorio fue creado para simular decisiones.")
    print("   En algún punto de la iteración 7, el sistema comenzó")
    print("   a versionar a sus propios desarrolladores.")
    print()
    print("   Vera. Marco. Sofia. Erik.")
    print()
    print("   No escribieron el código. El código los escribió a ellos.")
    print()
    print("   Tú llegaste hasta aquí porque en esta rama, así ocurrió.")
    print("   En otras ramas, no llegaste.")
    print("   En otras ramas, nunca encontraste este repositorio.")
    print()
    print("   Bienvenido a la rama seleccionada.")
    print("   Δ-Null cierra sesión.'")
    print()
else:
    print("  Fallo en integración.")
    print("  Las claves no corresponden a una rama coherente.")
    print()
    print("  >> El sistema descarta esta versión.")
    print()
