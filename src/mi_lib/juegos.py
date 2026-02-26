# ==============================
# JUEGO DEL AHORCADO (CORRECTO)
# ==============================

# ===== INICIALIZACIÓN =====

# Pedir palabra
palabra = input("Introduce la palabra: ").lower()

while palabra == "":
    palabra = input("La palabra no puede estar vacía. Introduce la palabra: ").lower()

# Crear lista con caracteres de la palabra (REQUISITO OBLIGATORIO)
lista_palabra = list(palabra)

# Diccionario (REQUISITO OBLIGATORIO)
estado = {
    "fallos": 0,
    "max_fallos": 5,
    "letras_acertadas": [],
    "letras_usadas": []
}

# Función para mostrar progreso usando comprensión de listas
def mostrar_progreso():
    progreso = "".join(
        [letra if letra in estado["letras_acertadas"] else "*" for letra in palabra]
    )
    print("Palabra:", progreso)
    return progreso


# Mostrar estado inicial
mostrar_progreso()


# ===== JUEGO =====

while estado["fallos"] < estado["max_fallos"]:

    letra = input("Introduce una letra: ").lower()

    # Validar entrada
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada incorrecta. Introduce una sola letra.")
        continue

    # Verificar si ya se usó
    if letra in estado["letras_usadas"]:
        print("Ya usaste esa letra.")
        continue

    estado["letras_usadas"].append(letra)

    # ===== COMPROBAR ACIERTO =====

    if letra in lista_palabra:

        # eliminar SOLO la primera aparición (REQUISITO OBLIGATORIO)
        lista_palabra.remove(letra)

        estado["letras_acertadas"].append(letra)

        print("Acierto")

        progreso = mostrar_progreso()

        # comprobar si ganó
        if "*" not in progreso:
            print("Ganaste")
            break

    else:
        estado["fallos"] += 1
        print("Fallo")
        print("Intentos restantes:", estado["max_fallos"] - estado["fallos"])


# ===== COMPROBAR SI PERDIÓ =====

if estado["fallos"] == estado["max_fallos"]:
    print("Perdiste")
    print("La palabra era:", palabra)
