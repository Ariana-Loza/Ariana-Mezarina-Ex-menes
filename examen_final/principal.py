import random


def aleatoria():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista aleatoria: {}".format(lista))
    return lista


def no_repetidos(lista):
    no_reps = list(set(lista))
    print("Números no repetidos: {}".format(no_reps))
    return no_reps


def ordenar_lista(lista):
    des = sorted(lista, reverse=True)
    asc = sorted(lista)
    print("Orden descendente: {}".format(des))
    print("Orden ascendente: {}".format(asc))
    return des, asc


def mayor_par(lista):
    mayor = 0
    for num in lista:
        if num % 2 == 0 and num > mayor:
            mayor = num
    print("Mayor número par: {}".format(mayor))
    return mayor
