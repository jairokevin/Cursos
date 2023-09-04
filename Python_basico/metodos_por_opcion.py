from continente import Continente
from pais import Pais
import json

DIC_RESPUESTAS = {}

# Para forzar la salida tal cual el enunciado
DIC_RESPUESTAS['respuesta1'] = {}
DIC_RESPUESTAS['respuesta2'] = {}
DIC_RESPUESTAS['respuesta3'] = {}

def mostrar_respuesta_final():
  for opcion , respuesta in DIC_RESPUESTAS.items():
    print(f'* {opcion} * => ')
    for clave , valor in respuesta.items():
      print(f' {clave}  ::  {valor}')
  print()

def mostrar_respuesta(res):
  for clave , valor in res.items():
    print(f' {clave}  ::  {valor}')
  print()

# Qué  continente tiene mayor población? y cuál es el número? 
def opcion_1(obj_continentes):
  max = 0
  conti = ''
  repuesta = {}
  for i in obj_continentes:
    if i.get_poblacion() > max :
      max = i.get_poblacion()
      conti = i.get_nombre()
  
  repuesta['mayor_poblacion'] = conti
  repuesta['numero'] = max
  DIC_RESPUESTAS['respuesta1'] = repuesta

  print('respuesta1 =>')
  mostrar_respuesta(repuesta)

# Suponiendo que la población habla en proporciones iguales cada idioma del 
# país. Qué idioma es el más hablado del mundo y cuál por cada continente? 

def opcion_2(obj_continentes):
  repuesta = {}
  mundial = ''  #idioma mas hablado
  uso_mundial = 0
  uso_continental = 0
  continental = ''
  idiomas_mundo = {}

  # Lo agrego primero para respetar el orden en el documento
  repuesta['World'] = mundial

  for i in obj_continentes:
    for clave, valor in i.get_lenguas().items():
      #Busco la lengua popular correspondiente al contienente
      if valor > uso_continental:
        continental = clave
        uso_continental = valor
      
      # Si no esta lo agrego al dic de idiomas mundial
      if idiomas_mundo.get(clave) == None:
        idiomas_mundo[clave] = valor
      else:
        idiomas_mundo[clave] += valor

    # Omito los continentes sin idioma, por ejemplo la Antartica
    if continental != '':
    # Agrego el idioma mas usado por continente mientras exista
      repuesta[i.get_nombre()] = continental
    # Seteo las variables para el siguiente continente
    continental = ''
    uso_continental = 0

  # Busco el idioma mas hablado en el mundo
  for idioma, cantidad in idiomas_mundo.items():
    if cantidad > uso_mundial :
      mundial = idioma
      uso_mundial = cantidad

  repuesta['World'] = mundial

  DIC_RESPUESTAS['respuesta2'] = repuesta

  print('respuesta2 =>')
  mostrar_respuesta(repuesta)

# Qué moneda se usa en más países y cuántos países son?
def opcion_3(obj_paises):
  cantidad_monedas = {} # Diccionadio de monedas por cantidad de paises
  repuesta = {}
  for pais in obj_paises:
    # Paso en limpio las monedad con la cantidad de paises que la usa
    if cantidad_monedas.get(pais.get_codigo()) == None:
      cantidad_monedas[pais.get_codigo()] = 1
    else:
      cantidad_monedas[pais.get_codigo()] += 1

  # Busco la moneda mas usada
  max = 0
  for moneda, cantidad in cantidad_monedas.items():
    if cantidad > max :
      moneda_buscada = moneda
      max = cantidad

  repuesta['moneda_mas_usada'] = moneda_buscada
  repuesta['cant_paises'] = max

  DIC_RESPUESTAS['respuesta3'] = repuesta

  print('respuesta3 =>')
  mostrar_respuesta(repuesta)

def guardar():
  with open('db/respuestas.json', 'w') as respuestas:
    json.dump(DIC_RESPUESTAS, respuestas , indent= 2)
