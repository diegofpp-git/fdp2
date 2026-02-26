def saluda(nombre):
  print("¡Hola {}!".format(nombre))

def tablero(dim, muros):
    filas, columnas = dim

    tab = [[' ' for numero in range(columnas)] for numero in range(filas)]

    # Validar que todos los muros están dentro de mi tablero

    for f, c in muros:
        tab[f][c] = 'X'

    # Plantear E y S como argumentos de la función

    tab[0][0] = 'E'
    tab[filas - 1][columnas - 1] = 'S'

    for fila in tab:
        print(fila)

    return tab


def numero_a_palabras(n):
    # Validar el rango
    if n < 0 or n > 999:
        return "Error: el número debe estar entre 0 y 999"

    # Diccionario de unidades
    unidades = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
        5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
    }

    # Diccionario del 10 al 15
    especiales = {
        10: "diez", 11: "once", 12: "doce",
        13: "trece", 14: "catorce", 15: "quince"
    }

    # Diccionario de decenas
    decenas = {
        2: "veinte", 3: "treinta", 4: "cuarenta",
        5: "cincuenta", 6: "sesenta",
        7: "setenta", 8: "ochenta", 9: "noventa"
    }

    # Diccionario de centenas
    centenas = {
        1: "ciento", 2: "doscientos", 3: "trescientos",
        4: "cuatrocientos", 5: "quinientos",
        6: "seiscientos", 7: "setecientos",
        8: "ochocientos", 9: "novecientos"
    }

    # Caso especial
    if n == 0:
        return "cero"

    if n == 100:
        return "cien"

    palabras = ""

    # Obtener centenas, decenas y unidades
    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    # Centenas
    if c > 0:
        palabras += centenas[c] + " "

    # Números entre 10 y 15
    if 10 <= n % 100 <= 15:
        palabras += especiales[n % 100]

    # Números entre 16 y 19
    elif 16 <= n % 100 <= 19:
        palabras += "dieci" + unidades[u]

    # Números entre 20 y 29
    elif 20 <= n % 100 <= 29:
        if u == 0:
            palabras += "veinte"
        else:
            palabras += "veinti" + unidades[u]

    # Decenas normales
    else:
        if d > 1:
            palabras += decenas[d]
            if u > 0:
                palabras += " y " + unidades[u]
        elif d == 0 and u > 0:
            palabras += unidades[u]

    return palabras.strip()


def numero_a_palabras(n):
    # Validar el rango
    if n < 0 or n > 999:
        return "Error: el número debe estar entre 0 y 999"
    
    # Diccionario de unidades
    unidades = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
        5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
    }

    # Diccionario del 10 al 15
    especiales = {
        10: "diez", 11: "once", 12: "doce",
        13: "trece", 14: "catorce", 15: "quince"
    }

    # Diccionario de decenas
    decenas = {
        2: "veinte", 3: "treinta", 4: "cuarenta",
        5: "cincuenta", 6: "sesenta",
        7: "setenta", 8: "ochenta", 9: "noventa"
    }

    # Diccionario de centenas
    centenas = {
        1: "ciento", 2: "doscientos", 3: "trescientos",
        4: "cuatrocientos", 5: "quinientos",
        6: "seiscientos", 7: "setecientos",
        8: "ochocientos", 9: "novecientos"
    }

    # Caso especial
    if n == 0:
        return "cero"

    if n == 100:
        return "cien"

    palabras = ""

    # Obtener centenas, decenas y unidades
    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    # Centenas
    if c > 0:
        palabras += centenas[c] + " "

    # Números entre 10 y 15
    if 10 <= n % 100 <= 15:
        palabras += especiales[n % 100]

    # Números entre 16 y 19
    elif 16 <= n % 100 <= 19:
        palabras += "dieci" + unidades[u]

    # Números entre 20 y 29
    elif 20 <= n % 100 <= 29:
        if u == 0:
            palabras += "veinte"
        else:
            palabras += "veinti" + unidades[u]

    # Decenas normales
    else:
        if d > 1:
            palabras += decenas[d]
            if u > 0:
                palabras += " y " + unidades[u]
        elif d == 0 and u > 0:
            palabras += unidades[u]

    return palabras.strip()

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
