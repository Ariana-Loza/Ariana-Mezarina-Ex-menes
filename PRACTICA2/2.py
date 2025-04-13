"""
EJERCICIO2:
- Crear una clase llamada Persona y agregar un atributo saldo a esta clase
(ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la clase Empleado que llame al método
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
deberá ir actualizando también el saldo o monto que tiene el otro empleado
en su cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando
una transferencia y con dos personas.
"""
class persona:
    def registrar_persona(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
        self.sueldo = float(input("Sueldo actual (S/): "))
        self.__saldo = float(input("Saldo actual en cuenta (S/): "))
        self.nacionalidad = "peruana"

    def mostrar_saldo(self):
        print("{} tiene un saldo actual de: "
              "S/ {:.2f}".format(self.nombre, self.__saldo))

    def transferir(self, monto, destino):
        if self.__saldo >= monto:
            self.__saldo -= monto

            destino.aumentar_saldo(monto)
            print("transferencia de S/ {:.2f} realizada de {} a {}.".format(monto, self.nombre, destino.nombre))

        else:
            print("Saldo insuficiente para realizar la transferencia.")

    def aumentar_saldo(self, monto):
        self.__saldo += monto


class empleado(persona):

    def aumento_sueldo(self):
        self.sueldo += self.sueldo * 0.30

empleado1 = empleado()
print("\n-- datos del primer empleado --")
empleado1.registrar_persona()
empleado1.aumento_sueldo()
print("{} tiene un sueldo actualizado de:"
      " S/ {:.2f}".format(empleado1.nombre, empleado1.sueldo))
empleado1.mostrar_saldo()

empleado2 = empleado()
print("\n-- Datos del segundo empleado --")
empleado2.registrar_persona()
empleado2.aumento_sueldo()
print("{} tiene un sueldo actualizado de: S/ {:.2f}".format(empleado2.nombre, empleado2.sueldo))
empleado2.mostrar_saldo()

while True:
    print("\n--- Transferencias ---")
    emisor = input("¿Quién realizará la transferencia? ({} / {}): ".format(empleado1.nombre, empleado2.nombre)).lower()
    if emisor == empleado1.nombre.lower():
        origen = empleado1
        receptor = empleado2
    elif emisor == empleado2.nombre.lower():
        origen = empleado2
        receptor = empleado1
    else:
        print("Nombre no válido.Intente de nuevo.")
        continue

    monto = float(input("Ingrese el monto a transferir: "))
    origen.transferir(monto, receptor)

    print("\n--- Saldos actuales ---")
    empleado1.mostrar_saldo()
    empleado2.mostrar_saldo()
    continuar = input("\n¿Desea realizar"
                      " otra transferencia? (si/no): ").lower()
    if continuar != "si":
        print("Fin del programa.")
        break
