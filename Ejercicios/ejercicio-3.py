# Importar el módulo sys para acceder a los argumentos de la línea de comandos
import sys

# Verificar si el usuario ingresó tres argumentos en la línea de comandos
if len(sys.argv) != 4:
    print("Uso: python3 ejercicio-3.py <ancho> <alto> <tipo_de_línea>")
    sys.exit(1)

# Obtener ancho, alto y tipo de línea de los argumentos
ancho = int(sys.argv[1])
alto = int(sys.argv[2])
tipo_de_línea = sys.argv[3]

# Definir los caracteres para los bordes según el tipo de línea
if tipo_de_línea == 'simple':
    esquina_superior_izq = '+'
    esquina_superior_der = '+'
    esquina_inferior_izq = '+'
    esquina_inferior_der = '+'
    horizontal = '-'
    vertical = '|'
elif tipo_de_línea == 'doble':
    esquina_superior_izq = '╔'
    esquina_superior_der = '╗'
    esquina_inferior_izq = '╚'
    esquina_inferior_der = '╝'
    horizontal = '═'
    vertical = '║'
else:
    esquina_superior_izq = tipo_de_línea
    esquina_superior_der = tipo_de_línea
    esquina_inferior_izq = tipo_de_línea
    esquina_inferior_der = tipo_de_línea
    horizontal = tipo_de_línea
    vertical = tipo_de_línea

# Imprimir la parte superior de la caja
print(esquina_superior_izq + horizontal * (ancho - 2) + esquina_superior_der)

# Imprimir los lados de la caja
for _ in range(alto - 2):
    print(vertical + ' ' * (ancho - 2) + vertical)

# Imprimir la parte inferior de la caja
print(esquina_inferior_izq + horizontal * (ancho - 2) + esquina_inferior_der)
