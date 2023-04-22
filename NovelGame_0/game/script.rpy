#Parece python pero no es python solo queda 
#validar ejecutando el juego

#Personajes
define athur=Character('Arthur',color="#FFDC2F")



#Inicio del juego
##Etiqueta de inicio
label start:
#Se agrega imagen y escena de castillo
image castle ="castle.png"
scene castle
with fade # se agrgega una transicion a la escena
"Historia inicial del Rey de Camelot"
#Se agrega imagen y escena interna del rey
image palacio="king-palace.png"
show palacio
with fade #se agrega transicion a la imagen
athur "Yo soy el que se convertira en el rey de Camelot" 