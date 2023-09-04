import json
from continente import Continente
from pais import Pais

PAIS_J = 'country'
CONTIENENTE_J = 'continent'
CODIGO_P_J = 'currency_code'
POBLACION = 'population'
LENGUAGES = 'languages'

def esta_en_list(lista, busqueda): 
  try:
    otro_indice = lista.index(busqueda)
    return True
  except:
    return False

def lectura():
  list_continentes = []  # Solo se usa para verificar en la carga
  obj_continentes = []   # Lista de objetos Continente
  obj_paises = []        # Lista de objetos Paises

  with open('db\country-by-continent.json') as file:
    lst_pais_continete = json.load(file)

  with open('db\country-by-currency-code.json') as file:
    pais_codigo = json.load(file)

  with open('db\country-by-population.json') as file:
    pais_poblacion = json.load(file)

  with open('db\country-by-languages.json') as file:
    pais_lenguajes = json.load(file)

  #Creo Objetos Paises
  for p in pais_codigo:
    obj_paises.append(Pais(p.get(PAIS_J), p.get(CODIGO_P_J)))

  # Recorro json con continentes
  for c in lst_pais_continete:
    # Creo objetos continente sino los cree
    if not esta_en_list(list_continentes, c.get(CONTIENENTE_J)):
      list_continentes.append(c.get(CONTIENENTE_J))
      obj_continentes.append(Continente(c.get(CONTIENENTE_J)))

    for conti in obj_continentes :
      # Objeto continente que en el que estoy trabajando
      if conti.get_nombre() == c.get(CONTIENENTE_J):
        #Busco el objeto continente para agregarlo en pais
        index_c = obj_continentes.index(conti)
        #Busco el objeto pais correspondiente al continente
        for pais_p in obj_paises:
          if pais_p.get_nombre() == c.get(PAIS_J):
            #index_p = obj_paises.index(pais_p)
            pais_p.set_continente(obj_continentes[index_c])

  # agrego la poblacion a cada pais y actualizo el continente
  for pob in pais_poblacion:
    for pais in obj_paises:
      if pob.get(PAIS_J) == pais.get_nombre():
        pais.set_poblacion(pob.get(POBLACION))
        pais.update_pob_cont()

  # Agrego las lenguas a cada pais
  for lenguas in pais_lenguajes:
    for pais in obj_paises:
      if lenguas.get(PAIS_J) == pais.get_nombre():
        for i in lenguas.get(LENGUAGES):
          pais.lenguaje.append(i)
        pais.update_lenguajes()

  return obj_paises, obj_continentes
