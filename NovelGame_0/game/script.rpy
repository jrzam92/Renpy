#Parece python pero no es python solo queda 
#validar ejecutando el juego

#Personajes
define narrador=Character('Narrador',color="#D9B90B")
define perseo=Character('Perseo',color="#0BE30F")
define r_acrisio=Character('Acrisio',color="#0099CC")
define oraculo=Character('Oraculo',color="#680BE3")
define m_danae=Character('Danae',color="#DB180D")
define d_jupiter=Character('Jupiter',color="#FFDC2F")
define pescador_dictis=Character('Dictis',color="#DC6E2C")
define r_polidectes=Character('Polidectes',color="#AB0BE3")
define medusa=Character('Medusa',color="#0099CC")
define d_mercurio=Character('Mercurio',color="#E30539")
define greas=Character('Greas',color="#0F22CC")
define gorgonas=Character('Gorgonas',color="#D9BC04")
define g_atlas=Character('Atlas',color="#C0D941")
define d_minerva=Character('Minerva',color="#7A48CC") 


#gorgonas-.- esteno,euriala,medusa
#sandalias, casco pluton . hoz de oro , escudo
#pegaso
#salida de caverna explosiva para no enfrentarse a las gorgonas 
#juegos olimpicos area de lanzamiento de disco mata a su abuelo 
#Se agrega imagen y escena interna del rey
# image palacio="king-palace.png"
# show palacio
# with fade #se agrega transicion a la imagen



  

#Inicio del juego
##Etiqueta de inicio
label start:
#Se agrega imagen y escena de castillo
image back ="back_story.jpg"

image im_narrador="narrador.jpg"
image im_perseo="perseo.jpg"
image im_r_acrisio_young="acrisio_young.jpg"
image im_r_acrisio_old="acrisio_old.jpg"
image im_oraculo="oraculo.jpg"
image im_m_danae="danae.jpg"
image im_d_jupiter="jupiter.jpg"
image im_pescador_dictis="dictis.jpg"
image im_r_polidectes="polidectes.jpg"
image im_medusa="medusa.jpg"
image im_d_mercurio="mercurio.jpg"
image im_greas="greas.jpg"
image im_gorgonas="gorgonas.jpg"
image im_g_atlas="atlas.jpg"
image im_d_minerva="Minerva.jpg"
image im_raul="raul.png"
scene back
with fade # se agrgega una transicion a la escena

show im_narrador
narrador "Iniciamos la historia en donde el rey Acrisio se encuentra en conversación con el Oráculo"
hide im_narrador

show im_r_acrisio_young
r_acrisio "¿Oráculo tendré hijos varones en mi futuro?"
hide im_r_acrisio_young

show im_oraculo
oraculo "No, usted Rey no tendrá hijos a un futuro"
hide im_oraculo 

show im_narrador
narrador "El oráculo no percibía las muertes repentinamente por lo que este le dice"
hide im_narrador
 
show im_oraculo
oraculo "Le comento su majestad que la forma de su muerte será por el hijo de su hija"
hide im_oraculo

show im_r_acrisio_young
r_acrisio "Tengo que hacer algo con mi hija Dánae, no puede tener hijos"
hide im_r_acrisio_young

show im_narrador
narrador "Él estaba pensando que hacer con la hija, no la podía matar porque si no quedaría mal como padre y entrando al castillo la hija le dice"
hide im_narrador

show im_m_danae
m_danae "¿Hola padre, Como te fue con el oráculo? ¿Que fue lo que te dijo?"
hide im_m_danae

show im_narrador
narrador "El padre le contesto…"
hide im_narrador

show im_r_acrisio_young
r_acrisio "Nada hija nada…"
hide im_r_acrisio_young

show im_narrador
narrador "El rey seguía pensando que hacer por lo que tomo la decisión de…"
hide im_narrador

show im_r_acrisio_young
r_acrisio "Ya sé que voy a hacer con mi hija la encerraré y así nadie podrá tener hijos con ella"
hide im_r_acrisio_young

show im_narrador
narrador "Por lo que el rey realiza tal acción, Dánae toda consternada no dice nada."
narrador "No esperaba que en unos de esos días, se le apareciera el dios Júpiter, este diciéndole"
hide im_narrador

show im_d_jupiter
d_jupiter "Veo que estás aquí sola, pero te puedo ayudar a escapar de las celdas"
hide im_d_jupiter

show im_m_danae
m_danae "De acuerdo, que debo hacer…"
hide im_m_danae

show im_narrador
narrador "A unos meses después, Dánae había tenido un varón, lo que pasaría después es…"
hide im_narrador

show im_r_acrisio_young
r_acrisio "¿Qué son esos berrinches?, Quien está llorando?"
hide im_r_acrisio_young

show im_narrador
narrador " Por lo que va hacia las celdas, viendo así a su hija con su nieto en brazos. Por lo que decide desterrarlos"
narrador "El rey le dice a unos de sus navíos que se los lleve muy lejos y que los deje caer lo más lejos del mar"
narrador "Pasa el tiempo y por fin llegan a una isla Dánae y su hijo, por los que fueron rescatados por un pescador el quien dijo…"
hide im_narrador

show im_pescador_dictis
pescador_dictis "¡O vaya!!! Me he encontrado un tesoro, veamos que trae dentro…"
hide im_pescador_dictis

show im_narrador
narrador "Dictis no pensaba que podría traer dos personas el cofre por lo que dijo …"
hide im_narrador

show im_pescador_dictis
pescador_dictis "Dios mío, no puedo creerlo, es una mujer y un niño. ¿Qué voy a hacer ahora?"
hide im_pescador_dictis

show im_narrador
narrador "Dánae le pregunta"
hide im_narrador

show im_m_danae
m_danae "¿Dónde nos encontramos?"
hide im_m_danae

show im_pescador_dictis
pescador_dictis "Ustedes se encuentran en la isla de Ciclades"
hide im_pescador_dictis

show im_narrador
narrador "Ellos se quedan a vivir con el pescador Dictis en su cabaña y ayudándolo con los deberes que se tenían que realizar"
narrador "El niño fue madurando y creciendo ayudando a Dictis a la pesca, Dánae de igual forma estaba muy agradecida con su benefactor por haberlos recogido y hospedado"
narrador "Pero un día llego el hermano de Dictis, el Rey Polidectes, quien le dijo a Dictis ..."
hide im_narrador

show im_r_polidectes
r_polidectes "¿Mi hermano, quien esa belleza, es tu esposa? ¿Tu princesa?"
hide  im_r_polidectes

show im_pescador_dictis
pescador_dictis "Ni una ni la otra, es alguien quien me encontré a las orillas de la isla, cuando estaba pescando."
hide im_pescador_dictis

show im_narrador
narrador "Por lo que rápidamente el rey le dijo a Dánae lo siguiente"
hide im_narrador

show im_r_polidectes
r_polidectes "Quiero que venga a mi castillo, no puede estar en esta cabaña y con este pescador, recibirá lo que merece el castillo"
hide im_r_polidectes

show im_narrador
narrador"Por lo que Dánae, quiere la opinión de Dictis para saber qué hacer ..."
hide im_narrador

show im_m_danae
m_danae "¿Sr. Dictis, usted fue quien nos salvó y agradezco eso, pero es necesario que vaya con el Rey?"
hide im_m_danae

show im_pescador_dictis
pescador_dictis "Es correcto, es necesario que vayas con el Rey"
hide im_pescador_dictis

show im_narrador
narrador "Dánae no quería irse con el rey, pero ella terminó aceptando, pero diciéndole al rey ..."
hide im_narrador

show im_m_danae
m_danae "Iré con usted con una condición, déjeme llevar a mi hijo Perseo"
hide im_m_danae

show im_narrador
narrador "El rey, aceptando la condición, vio de reojo a Perseo y dijo..."
hide im_narrador

show im_r_polidectes
r_polidectes "Él puede que sea un estorbo, pero haré lo que pueda para deshacerme de su hijo"
hide im_r_polidectes

show im_narrador
narrador "Unos meses ya habían pasado en el palacio Dánae y Perseo con la hospitalidad del rey, quien ese día cumplía años, por lo que estaba recibiendo regalos, pero este le pregunta a Perseo"
hide im_narrador

show im_r_polidectes
r_polidectes "¿Perseo que opinas de estos regalos?"
hide im_r_polidectes

show im_narrador
narrador "Por lo que Perseo contesta..."
hide im_narrador

show im_perseo 
perseo "Considero que estos regalos son muy ordinarios"
hide im_perseo

show im_r_polidectes
r_polidectes "¿Qué tipo de regalo crees que sea ideal para un rey?"
hide im_r_polidectes

show im_perseo 
perseo "Creo que sería la cabeza de medusa"
hide im_perseo

show im_r_polidectes
r_polidectes "Veo que no me has traído un regalo, Perseo"
r_polidectes "¿Por lo que tomaré tu palabra, quiero que me traigas la cabeza de Medusa, estás de acuerdo?"
hide im_r_polidectes

show im_perseo 
perseo "¡De acuerdo traeré la cabeza de Medusa!!!"
hide im_perseo

show im_narrador
narrador "Perseo decidido por ir por la cabeza de medusa, su madre Dánae trataba de que él no fuera, pero él al final decidió ir en la búsqueda para traer la cabeza de la Gorgona"
narrador "Embarcándose a una aventura no sabía hacia donde dirigirse, por lo que el dios Mercurio se le apareció y le dijo"
hide im_narrador

show im_d_mercurio
d_mercurio "¿Veo que no sabes por donde empezar tu búsqueda?"
hide im_d_mercurio

show im_perseo 
perseo "Es correcto, No sé donde se encuentra Medusa y hacia donde me debo de dirigir..."
perseo "¿Tú sabras en donde la puedo encontrar?"
hide im_perseo

show im_d_mercurio
d_mercurio "Sé quien podría ayudarte, pero debes de saber engañarlas para que ellas te digan la ubicación de donde se encuentra Medusa"
d_mercurio "¡Te llevaré, sube a mi espalda!"
hide im_d_mercurio

show im_narrador
narrador "Así iniciaron el viaje y al llegar Mercurio le dice... "
hide im_narrador

show im_d_mercurio
d_mercurio "Muchacho ten mi hoz de oro, aquí te dejo, mucha suerte. Los dioses están de tu lado."
hide im_d_mercurio

show im_narrador
narrador "Perseo, agradecido por el regalo que le dijo Mercurio, decidió continuar su camino."
narrador "Al encontrarse con las hermanas Greas,  Perseo vio que se estaban pasando un ojo y un diente, por lo que él rápidamente los tomo y dijo"
hide im_narrador

show im_perseo 
perseo "Les entregaré el ojo y el diente con dos condiciones... "
perseo "Una quiero que me digan donde puedo encontrar a Medusa y la otra que me den las herramientas para poder vencerla"
hide im_perseo

show im_narrador
narrador "Las Greas al no tener ojo, no podían llorar por lo que una de ellas le dijo"
hide im_narrador

show im_greas
greas "Bien, aceptamos el trato, por lo que Medusa se encuentra más haya de los horizontes de la Tierra, donde se encuentra el coloso Atlas, pero ella no está sola, se encuentra con sus hermanas Gorgonas"
greas "Te damos estas sandalias voladoras y este casco de Plutón, sabrás el momento de ocuparlo"
hide im_greas

show im_perseo 
perseo "¡Les devuelvo el ojo y el diente, gracias por la información y los objetos!!!"
hide im_perseo

show im_narrador
narrador "Así Perseo fue a la busca de Medusa y con la ayuda de las sandalias voladoras, no tardo en llegar a su destino"
narrador "Una vez que llego a su destino, se le apareció la diosa Minerva, diciéndole ..."
hide im_narrador

show im_d_minerva
d_minerva "Perseo, antes que vayas a enfrentar a Medusa, quiero darte este escudo, así como dijo Mercurio, nosotros estamos de tu lado, este escudo te ayudara a vencer a Medusa"
hide im_d_minerva

show im_perseo
perseo "Se lo agradezco mucho, estaba preocupado, estaba pensando muchas cosas, pero con este escudo, sé que podré vencerla."
perseo "Gracias!!!"
hide im_perseo


show im_narrador
narrador "Así, Perseo, ya con el escudo de la diosa Minerva, con la hoz de Mercurio, con el bolso mágico y el casco, se lanzó por la cabeza de Medusa."
hide im_narrador

show im_perseo
perseo "De acuerdo parece que ya llegue por lo que ahora tendré que ubicarlas y con este escudo podré ver donde se encuentran sin ver directamente"
perseo "Veo que están durmiendo quien será Medusa, parece que es la de en Medio, tengo que hacer el corte rápido y salir corriendo"
hide im_perseo

show im_narrador
narrador "Así Perseo logro hacer el corte de la cabeza y salió corriendo, ya que las hermanas se despertaron y vieron que solo estaba el cuerpo, por lo que empezaron a seguir a Perseo"
hide im_narrador

show im_gorgonas 
gorgonas "Alguien degolló a nuestra hermana Medusa, nos la pagará el quién haya realizado dicha acción"
hide im_gorgonas 

show im_narrador
narrador "Algo raro estaba dando forma saliendo del cuerpo de Medusa y era el nacimiento de Pegaso, el caballo alado."
narrador "Por lo que Pegaso, fue galopando a la ayuda de Perseo..."
hide im_narrador

show im_perseo
perseo "O vaya Pegaso, gracias por venir a mi ayuda, vámonos de este lugar... "
hide im_perseo

show im_narrador
narrador "Perseo se subió a Pegaso y le dijo ... "
hide im_narrador

show im_perseo
perseo "Pegaso, regresemos a la isla Ciclades a entregar este regalo al rey Polidectes"
hide im_perseo

show im_narrador
narrador "Una vez que llego Perseo a la isla a entregar el regalo, no encontraba al rey"
narrador "Pero el rey estaba buscando a Dánae, quien lo había rechazado."
narrador "Por lo que Perseo pidió una reunión con el rey y sus allegados para mostrar que había traído la cabeza de Medusa"
hide im_narrador

show im_perseo
perseo "Rey, le traigo aquí la cabeza de Medusa"
hide im_perseo

show im_r_polidectes
r_polidectes "¿Qué? ¿Crees que te voy a creer que traes en esa bolsita la cabeza de Medusa? Hahahaha!!! No te creo..."
hide im_r_polidectes

show im_narrador
narrador "Perseo, enojado por dentro, dijo ..."
hide im_narrador

show im_perseo
perseo "Es cierto, aquí traigo la cabeza de Medusa, esta bolsa es mágica"
hide im_perseo


show im_medusa
narrador "Por lo que Perseo mostró la cabeza de Medusa al rey y este ni le dio tiempo de realizar nada, ya que se había quedado petrificado en piedra"
 

narrador "Los a llegados al rey querían venganza, pero Perseo, también les muestra la cabeza y quedan petrificados" 
hide im_medusa


show im_narrador
narrador "Así se fue con su madre Dánae y con el pescador Dictis, para tomar el trono de Argos, donde es el único reino que puede reinar."
narrador "El rey Acrisio se entera de que su hija y su nieto sobrevivieron y venían hacia Argos, por lo que este se exilia."
hide im_narrador

show im_narrador
narrador "Un día en unos juegos olímpicos donde estaba participando Perseo en la sección de tiro de disco, estaba Acrisio en las bardas hasta arriba y este le pregunta a una persona que estaba a lado de él ... "
show im_narrador

show im_r_acrisio_old
r_acrisio "¿Disculpa, Por qué tiene miedo este jugador de lanzar el disco?"
hide im_r_acrisio_old

show im_pescador_dictis
pescador_dictis "No es que tenga miedo de lanzar el disco, tiene miedo que si al lanzarlo pueda matar a una persona de las bardas"
show im_pescador_dictis

show im_r_acrisio_old
r_acrisio "¿Y este jugador como se llama?"
hide im_r_acrisio_old

show im_pescador_dictis
pescador_dictis "Es \"Perseo\" nieto del rey Acrisio y quien degolló a Medusa, una de las hermanas gorgonas"
hide im_pescador_dictis

show im_r_acrisio_old
r_acrisio "¿Qué? ... Es Perseo!, no ... Tengo que irme de aquí ..."
hide im_r_acrisio_old

show im_narrador
narrador "En el momento que el rey Acrisio se estaba yendo, su destino era morir por su nieto, por lo que el disco degolló al rey."
narrador "Por lo que Perseo, viendo quien era, tuvo que reinar Argos"
narrador "Espero que esta historia haya sido de su agrado"
narrador "Esta es una adaptación de \"Cuentos y leyendas de los héroes de la mitología\" por \"Christian Grenier\" y \"Philippe Kailhenn\""
narrador "Las imágenes se sacaron de una IA para ver su forma dentro de las novelas, o bien que sea solo un prototipo"
narrador "Adaptacion realizada por ..."
hide im_narrador

show im_raul
narrador "Jose Raul Zamora Villaseñor"
hide im_raul

