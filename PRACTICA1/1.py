nombre="Ariana Mezarina"
salario=4000
edad="21"
compañia="Universidad Nacional Mayor de San Marcos"
print(type(nombre))
print(type(salario))
print(type(edad))
print(type(compañia))

edad2=int(edad)
print(type(edad2))

if edad2>30:
    bono1=salario*0.1
    print("Usted tiene un bono de 10% en el mes de diciembre")
if edad2<30:
    bono1=salario*0.05
    print("Usted tiene un bono del 5% en el mes diciembre")

bono_final=pow(bono1,2)
print(bono_final)

