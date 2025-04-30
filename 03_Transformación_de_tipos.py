###
#Curso de python desde 0, primero empecezamos con un Hola mundo
# #03 - Casting de tipos de datos
# Transformar un tipo de valor a otro
###

print ("Conversión de tipos de datos")

print(type("100"))
#Python no realiza conversiones automaticas entre tipos incompatible
#python tiene un tipado Fuerte (aunque es un lenguaje no tipado :v)
#Tenemos que transformarlo nosotros

print(type(int("100")))

print(2+ int("100"))
# ó
print ("100" + str(2)) #Concatenación de cadenas de texto (Que no sumar)

#Se puede redondear
print(round(3.1416)) #Redondea al entero más cercano

print(round(2.5)) #Redondea a 2
print(round(3.5)) #Redondea al entero par más cercano | Redondea a 4

print(float("3.1416"))
#Tambien podemos:
print (int (3.1416)) #Redondea hacia abajo

print(bool(3))
print(bool(0)) #0 es falso | Es el unico númerico que se transforma como negativo
print (bool(-1)) #No se hace falso | -1 es verdadero


print(bool("")) #"" es falso 
print(bool(" ")) #Espacio en blanco es verdadero
print(bool("False")) #"False" es verdadero porque es una cadena de texto | No se hace falso

#Tambien hay casos como: 
#print(int("Hola mundo"))