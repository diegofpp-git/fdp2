import urllib.request
import smtplib
from email.message import EmailMessage

# =======================
# FUNCIONES
# =======================

def descargar_google_doc(url):
    partes = url.split("/")
    doc_id = partes[5]
    url_txt = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"

    with urllib.request.urlopen(url_txt) as response:
        contenido = response.read().decode("utf-8")

    return contenido


def calcular_estadisticas(texto):
    palabras = len(texto.split())
    caracteres = len(texto)
    caracteres_sin_espacios = len(texto.replace(" ", "").replace("\n", ""))

    return palabras, caracteres, caracteres_sin_espacios


def guardar_txt(texto, nombre):
    with open(nombre, "w", encoding="utf-8") as f:
        f.write(texto)


def enviar_email(remitente, password, destinatario, asunto, cuerpo, archivo):

    msg = EmailMessage()
    msg["From"] = remitente
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg.set_content(cuerpo)

    with open(archivo, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype="text",
                           subtype="plain",
                           filename=archivo)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(remitente, password)   # usar APP PASSWORD
        smtp.send_message(msg)


# =======================
# PROGRAMA PRINCIPAL
# =======================

try:

    # URL del documento
    url = input("Introduce la URL del Google Doc: ")

    contenido = descargar_google_doc(url)

    # Estadísticas
    palabras, caracteres, sin_espacios = calcular_estadisticas(contenido)

    print("Palabras:", palabras)
    print("Caracteres:", caracteres)
    print("Caracteres sin espacios:", sin_espacios)

    # Guardar archivo
    archivo = "documento.txt"
    guardar_txt(contenido, archivo)

    # Datos email
    remitente = input("Introduce tu Gmail: ")
    password = input("Introduce tu APP PASSWORD de Gmail: ")
    destinatario = input("Introduce el destinatario: ")
    asunto = input("Introduce el asunto: ")

    cuerpo = f"""
Estadísticas del documento:

Palabras: {palabras}
Caracteres: {caracteres}
Caracteres sin espacios: {sin_espacios}

Se adjunta el documento en formato TXT.
"""

    enviar_email(remitente, password, destinatario, asunto, cuerpo, archivo)

    print("Email enviado correctamente.")

except Exception as e:
    print("Error:", e)
