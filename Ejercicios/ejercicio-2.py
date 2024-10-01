texto = input("Introduce una cadena de texto: ")

reemplazar_letras = {
    'O' : '0',
    'I' : '1',
    'E' : '3',
    'A' : '4',
    'S' : '5',
    'G' : '6',
    'T' : '7',
    'B' : '8',
    'g' : '9'  
}

texto_cifrado = ""

for letra in texto:
    texto_cifrado += reemplazar_letras.get(letra, letra)


print(f"Texto: {texto}")
print(f"Texto nuevo: {texto_cifrado}")
