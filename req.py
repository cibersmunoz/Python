import requests

url = "https://google.com"

respuesta = requests.get(url)

print(respuesta.status_code)

#if respuesta.status_code==200:
#    print("El servidor ha respondido OK")
#print(respuesta.cookies)
#print(respuesta.headers)
#print(respuesta.content)
#print(respuesta.text)
#print(respuesta.links)

def url_extractor(text):
    urls = []
    for word in text.split():
        if 'http' in word:
            urls.append(word)
    return urls

links = (url_extractor(respuesta.text))

for link in links:
    print(link)