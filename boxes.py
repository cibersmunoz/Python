#ASCII ART DIAGRAMS en github


#Este programa dibujará cajas en la terminal dados el ancho y el alto de los mismos

#Por ejemplo, con ancho = 3 y alto = 6, tendriamos:

# 123
#┌──┐
#│  │
#│  │   
#│  │
#│  │  
#│  │
#│  │
#└──┘


import sys

print(sys.argv)
ancho = int(sys.argv[1])
alto = int(sys.argv[2])
tipo = sys.argv[3]



chars_simple = "┌┐┘└│─"
chars_doble= "012345"
espacio=" "

#Pedimos la anchura
#ancho = int(input("Introduzca la anchura : "))

if tipo == "simple":
        chars = chars_simple
else: 
        chars = chars_doble





#print("┌" + "─" * ancho + "┐")
def makeline(start, fill, end, ancho):
        print(start,fill,end,ancho)
        return (start + fill * ancho + end)
makeline (chars_simple[0], chars_simple[len(chars_simple)-1], chars_simple[1], ancho)