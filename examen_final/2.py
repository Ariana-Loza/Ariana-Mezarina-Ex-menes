"""
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.
- La función que vas a crear va a capturar, la edad, nombre, hora y minuto en
que fue registrado la persona (usar la librería correspondiente)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La que función que será decorada calculará la media de 4 notas.
"""

from datetime import datetime


def decorar(func):
    def funcion_a(*args, **kwargs):
        if len(args) + len(kwargs) <= 1:
            print("La función necesita más de un parámetro para ejecutarse.")
            return None
        resultado = func(*args, **kwargs)
        print("La función ejecutó.")
        return resultado
    return funcion_a


def persona(nombre, edad):
    ahora = datetime.now()
    hora = ahora.hour
    minuto = ahora.minute
    print("{} de {} años ha sido registrado a las {} horas"
          " con {} minutos".format(nombre, edad, hora, minuto))


@decorar
def media(n1, n2, n3, n4):
    resultado = (n1 + n2 + n3 + n4) / 4
    print("La media de las notas es: {}".format(resultado))
    return resultado


persona("Pedro", 30)
media(15, 18, 12, 19)
