###
#Curso de python desde 0, primero empecezamos con un Hola mundo
# #02 - Tipos de datos
# # En python existen varios tipos de datos, los más comunes son:
# # - int (números enteros)
# # - float (números decimales)
# # - str (cadenas de texto)
# # - bool (booleanos: True o False)
# # - list (listas)
# # - NoneType (nada)
    

print ("int: ")
# Todos estos son enteros
print (10)
print (150)

#Podemos poner que nos diga el tipo del valor que se encuentra dentro de cada print
print ("El tipo de dato es: ", type(10)) #Estan envueltos con la función type
print ("El tipo de dato es: ", type(0))
print ("El tipo de dato es: ", type(-5))

print (end= "/n" "float: ")
print (10.5)
print (150.5)
print (type(10.5)) #float es un número decimal
print (type(150.5))
print (type(1e3)) #float es un número decimal | 1e3 es 1000.0 Tambien se puede poner con notación científica

print (end= "/n" "complex: ") #números complejos
print (10j) #10j es un número complejo
print (type(10 +2j)) #10j es un número complejo

print (end= "/n" "str: ") #cadenas de texto
print ("Hola Mundo")
print ("Hola Mundo", type("Hola Mundo")) #Hola Mundo es una cadena de texto
print (type("123"))

print (end= "/n" "bool: ") #booleanos
print (True) #True es un booleano
print (False) #False es un booleano
print (type(True)) #True es un booleano
print (type(1<2)) #Devuelve un boolenao

print (end= "/n" "NoneType: ") #Representa la ausencia de valor
print (type(None)) #None es un tipo de dato especial que representa la ausencia de valor
