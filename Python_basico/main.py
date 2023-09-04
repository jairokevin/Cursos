import os
from leer_json import lectura
from metodos_por_opcion import opcion_1, opcion_2, opcion_3
from metodos_por_opcion import guardar, mostrar_respuesta_final


def opcion():
  op = input("\U0001F58B  ► ")

  if op.isdigit():
    if int(op)<1 or int(op)> 4:
      print(f'{op} \U0000274C no es una opcion valida \U000026A0')
      return opcion()
    return int(op)
  else:
    print(f'{op} \U0000274C no es una opcion valida \U000026A0')
    return opcion()

def pantalla_principal():
  print('\U000026A0 Solo se guardaran las respuestas que solicite')
  print('Elija una opcion \U00002714')
  print('1 - Continente de mayor población \U0001F5FA')
  print('2 - Idioma mas usado \U0001F520 por continente \U0001F30E ')
  print('3 - Moneda mas usada \U0001F4B2 \U0001F4B5 por país')
  print('4 - Salir \U0001F534')
  op = opcion()

  return op

#********
# Main
#********
def run():
    os.system('cls') # Limpio la consola antes de mostrar el menu
    print("Bienvenido!  \U0001F600".center(50))
    obj_paises, obj_continentes = lectura()
    #Menú principal
    salir = False

    while not salir:
        opcion = pantalla_principal()

        if opcion == 1:
          opcion_1(obj_continentes)

        elif opcion == 2:
          opcion_2(obj_continentes)

        elif opcion == 3:
            opcion_3(obj_paises)

        elif opcion == 4:
            salir = True
            mostrar_respuesta_final()
    guardar()

    exit()

if __name__ == "__main__":
    run()