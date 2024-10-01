import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Comprobador enlaces")
    parser.add_argument("path", help="El archivo a analizar")
    return parser.parse_args()


def iterar_archivo(path, funcion):
    try:
        with open(path,"r") as archivo:
            for linea in archivo:
                limpio = linea.strip() # Elimina espacios en blanco y saltos de linea
                funcion(limpio)
    except FileNotFoundError:
        print("Ese archivo no existe")
    except Exception as error:
        print("[Error]" + error)

def check_status(url):
    url = add_protocol(url)
    try:
        respuesta = requests.get(url, timeout=5)
        print(respuesta.status_code, url)
        write_file(respuesta.status_code, url)
    except requests.exceptions.RequestException as error:
        print(f"[Error] {error}") 

def add_protocol(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
        return url
    else:
        return url
    
def write_file(code, url, file="resultados.txt"):
    with open(file, "a") as f:
        f.write(f"[{code}] - {url}\n")
    
def capitalize(string):
    print(string.upper())

args = parse_args()


iterar_archivo(args.path, check_status)

