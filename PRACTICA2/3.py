"""
EJERCICIO 3:
- El programa deberá considerar 2 cuentas bancarias: 1 en soles y
otra en dólares. Considerar el nombre y apellido del titular
- Deberá tener un método para transferir entre sus cuentas, pero
para realizar esto debe hacer una conversión de monedas.
- Tendrá otro método para retirar dinero, esto debe actualizar ambas
cuentas y mostrar en pantalla los montos actualizados, a su vez
validar si tiene fondos suficientes o no para el retiro, mostrar un
mensaje que indique no tiene suficientes en caso fuera el caso.
- Instanciar 3 veces los casos de transferencias para ver reflejado el
uso de tus métodos creados.
"""
print("Registro de billetera digital")
nombre = input("Nombre: ")
apellido = input("Apellido: ")

cuenta_soles = float(input("Saldo en soles: "))
cuenta_dolares = float(input("Saldo en dólares: "))

cambio = 3.8

print("\nRealiza 3 transferencias entre tus cuentas:")
n = 1
while n <= 3:
    print("\nTransferencia", n)
    print("1. De soles a dólares")
    print("2. De dólares a soles")
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        monto = float(input("Monto en soles a transferir: "))
        if cuenta_soles >= monto:
            cuenta_soles -= monto
            cuenta_dolares += monto / cambio
            print("Transferencia realizada.")
        else:
            print("Saldo en soles insuficiente.")
    elif opcion == "2":
        monto = float(input("Monto en dólares a transferir: "))
        if cuenta_dolares >= monto:
            cuenta_dolares -= monto
            cuenta_soles += monto * cambio
            print("Transferencia completada.")
        else:
            print("Saldo en dólares insuficiente.")
    else:
        print("Opción inválida.")

    print("Saldo actual en soles: S/ {:.2f}".format(cuenta_soles))
    print("Saldo actual en dólares: $ {:.2f}".format(cuenta_dolares))
    n += 1

print("\nRetiro de dinero")
print("1. Retirar en soles")
print("2. Retirar en dólares")
opcion_retiro = input("Elige una opción (1 o 2): ")

if opcion_retiro == "1":
    retiro = float(input("Monto a retirar en soles: "))
    if cuenta_soles >= retiro:
        cuenta_soles -= retiro
        print("Retiro realizado.")
    else:
        print("No hay saldo suficiente en soles.")
elif opcion_retiro == "2":
    retiro = float(input("Monto a retirar en dólares: "))
    if cuenta_dolares >= retiro:
        cuenta_dolares -= retiro
        print("Retiro realizado.")
    else:
        print("No hay saldo suficiente en dólares.")
else:
    print("Opción inválida.")

print("\nResumen final")
print("Titular: {} {}".format(nombre, apellido))
print("Saldo final en soles: S/ {:.2f}".format(cuenta_soles))
print("Saldo final en dólares: $ {:.2f}".format(cuenta_dolares))
