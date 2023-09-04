
class Continente:
  def __init__(self, nombre):
    self.nombre = nombre
    self.paises = []
    self.poblacion = 0
    # Dic constituido por "lengua" : "cantidad de paises que la usa" dentro del 
    # coninente
    self.lenguas = {} 

  def agregar_pais(self, pais):
    self.paises.append(pais)

  def get_nombre(self):
    return self.nombre

  def get_poblacion(self):
    return self.poblacion

  def get_lenguas(self):
    return self.lenguas

  def get_paises(self):
    return self.paises

  def actualizar_poblacion(self, cant):
    self.poblacion += cant

  # Agregar una nueva lengua e indicarle que al menos 1 pais la usa
  def agregar_lengua(self, lengua):
    self.lenguas[lengua] = 1 

  # Aumenta en 1 la cantidad de paises que usa esa lengua
  def aumentar_uso_lengua(self, lengua):
    self.lenguas[lengua] += 1

  # Toma una lista de lenguas y autaliza el dic lenguas
  def actualizar_lenguas(self, list_leng):
    for i in range(len(list_leng)):
      if self.lenguas.get(list_leng[i], -1) == -1 :
        self.agregar_lengua(list_leng[i])
      else:
        self.aumentar_uso_lengua(list_leng[i])

  # Devuelve el pais y la cantida de la lengua mas usada en contienente
  def get_lengua_popular(self):
    cantidad = -1
    for clave, valor in self.get_lenguas().items():
      if valor > cantidad:
        pais = clave
        cantidad = valor
    return pais, cantidad

