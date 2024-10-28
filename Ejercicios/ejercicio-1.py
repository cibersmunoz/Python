# Importar el módulo sys para acceder a los argumentos de la línea de comandos
import sys

# Diccionario para mapear ARN a ADN
mapa_arn_adn = {'A': 'A', 'U': 'T', 'G': 'G', 'C': 'C'}

# Obtener la secuencia de ARN del argumento
arn = sys.argv[1]

# Variable para almacenar la secuencia de ADN
adn = ''

# Recorrer cada carácter de la secuencia ARN
for letra in arn:
    # Verificar si el carácter es válido (A, U, G o C)
    if letra not in mapa_arn_adn:
        print("Error: Secuencia ARN inválida. Ingresa solo A, U, G o C.")
        sys.exit(1)
    
    # Convertir el carácter de ARN a ADN y añadirlo a la secuencia ADN
    adn += mapa_arn_adn[letra]

# Imprimir la secuencia de ADN
print("Secuencia ADN:", adn)

