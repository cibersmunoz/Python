# Importar el módulo sys para acceder a los argumentos de la línea de comandos
import sys

# Diccionario para mapear los caracteres a su equivalente en 13375P34K
clave_sustitucion = {
    'O': '0', 
    'I': '1',
    'E': '3', 
    'A': '4', 
    'S': '5', 
    'G': '9', 
    'T': '7', 
    'B': '8', 
}

# Obtener el texto del argumento
texto = sys.argv[1]

# Variable para almacenar el texto en cifrado
resultado = ''

# Recorrer cada carácter del texto
for letra in texto:
    # Sustituir el carácter si está en el diccionario, si no, dejarlo igual
    if letra in clave_sustitucion:
        resultado += clave_sustitucion[letra]
    else:
        resultado += letra

# Imprimimos el texto
print("Texto:", resultado)
