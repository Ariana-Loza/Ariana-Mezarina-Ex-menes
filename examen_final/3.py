"""
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con minutos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos.
"""

from datetime import datetime


def funcion_decorar(func):
    def fun_b(**kwargs):
        ahora = datetime.now()
        print("El decorador está siendo ejecutado a "
              "las {} con {} minutos".format(ahora.hour, ahora.minute))

        suma = sum(kwargs.values())
        print("La suma de los elementos es: {}".format(suma))

        resultado = func(**kwargs)
        return resultado
    return fun_b


@funcion_decorar
def mayor(**numeros):
    mayor_num = max(numeros.values())
    print("El mayor número es: {}".format(mayor_num))
    return mayor_num


print("\n--- Ejemplo 1 ---")
mayor(a=5, b=12, c=3, d=9, e=15, f=7)

print("\n--- Ejemplo 2 ---")
mayor(x=20, y=40, z=10)

print("\n--- Ejemplo 3 ---")
mayor(n1=2, n2=4, n3=6, n4=8)
