# Importamos módulos necesarios
import subprocess
import sys
import time

# Verificamos si se proporcionaron los argumentos necesarios
if len(sys.argv) != 6:
    print("Error: debes introducir nombre_archivo.py <dirección_ip> <num_solicitudes> <tamaño_paquete> <tiempo_espera> <retraso>")
    sys.exit(1)

# Obtener los argumentos de la línea de comandos
direccion_ip = sys.argv[1]
num_solicitudes = int(sys.argv[2])
tamano_paquete = int(sys.argv[3])
tiempo_espera = int(sys.argv[4])
retraso = float(sys.argv[5])

# Ejecutar el comando ping repetidamente
for _ in range(num_solicitudes):
    comando = f"ping -c 1 -s {tamano_paquete} -W {tiempo_espera} {direccion_ip}"
    subprocess.run(comando, shell=True)
    time.sleep(retraso)
