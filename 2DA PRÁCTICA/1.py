"""
EJERCICIO 1:
- Crear una clase llamada Empleado donde sus atributos deben ser nombre,
edad, sueldo y de nacionalidad peruana, tendrá un método para solicitar su
nombre y otro para solicitar su edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Empleado y usar su nuevo método
aumentoSueldo para incrementar su sueldo en un 30% (mínimo instanciar
la clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
- Crear un siguiente método que retorne un mensaje donde indique que: “En
el año XXXX tendrá XX años”, el año se ingresará por parámetro y la
edad también, realizar una validación si la edad ingresada por parámetro
es menor a la del constructor indicar que no es posible realizar la
operación (Mostrar por pantalla este valor)

"""
class empleado:
    def registrar(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        self.saldo = float(input("Ingrese su sueldo actual (S/): "))
        self.nacionalidad = "Peruana"

    def cumpleaños(self):
        self.edad += 1

    def aumento_sueldo(self):
        self.saldo += self.saldo * 0.30

    def edad_verificada(self, año, edad_ingresada):
        if edad_ingresada < self.edad:
            return "No se puede calcular. La edad ingresada es menor a la actual."
        else:
            return "En el año {} tendrá {} años.".format(año, edad_ingresada)


empleado1 = empleado()
print("\n-- Datos del primer empleado --")
empleado1.registrar()
empleado1.aumento_sueldo()
print("\n{} tiene un sueldo actualizado de: S/ {:.2f}".format(empleado1.nombre, empleado1.saldo))

año1 = int(input("Ingrese un año a proyectar para {}: ".format(empleado1.nombre)))
edad_proyectada1 = int(input("Ingrese la edad que tendría en {}: ".format(año1)))
print(empleado1.edad_verificada(año1, edad_proyectada1))


empleado2 = empleado()
print("\n-- Datos del segundo empleado --")
empleado2.registrar()
empleado2.aumento_sueldo()
print("\n{} tiene un sueldo actualizado de: S/ {:.2f}".format(empleado2.nombre, empleado2.saldo))

año2 = int(input("Ingrese un año a proyectar para {}: ".format(empleado2.nombre)))
edad_proyectada2 = int(input("Ingrese la edad que tendría en {}: ".format(año2)))
print(empleado2.edad_verificada(año2, edad_proyectada2))

