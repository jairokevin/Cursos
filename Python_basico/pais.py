from continente import Continente

class Pais:

  def __init__(self, nombre, codigo):
    self.nombre = nombre   # String
    self.codigo = codigo   # moneda
    self.poblacion = 0     # Int
    self.lenguaje = []
    self.provincias = []
    self.continente = None

  def get_continente(self):
    return self.continente

  def set_continente(self, contienete):
    self.continente = contienete

  def get_nombre(self):
    return self.nombre

  def get_codigo(self):
    return self.codigo

  def get_poblacion(self):
    return self.poblacion

  def get_lenguaje(self):
    return self.lenguaje

  def get_provincias(self):
    return self.provincias

  def set_poblacion(self, cantidad):
    self.poblacion = cantidad

  def add_lenguaje(self, lengua):
    self.lenguaje.append(lengua)

  def add_provincia(self, prov):
    self.provincias.append(prov)

  # suma la poblacion del pais a la poblacion del continente al que corresponde
  def update_pob_cont(self):
    self.continente.actualizar_poblacion(self.get_poblacion())

  # Agrega los idiomas del pais a los idiomas del continente al que corresponde
  def update_lenguajes(self):
    self.continente.actualizar_lenguas(self.get_lenguaje())
