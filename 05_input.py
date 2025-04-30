###
#Curso de python desde 0, primero empecezamos con un Hola mundo
# #05 - Entrada de usuario (input()) - Versión simplificada
# la función input() permite obtener datos al usuario a traves de la consola
###

print("Hola, como te llamas Chacho?")
nombre = input()

print(f"HolaM {nombre}, bienvenido al curso de python desde 0")

age = input("Cuantos años tienes?") #Toda la información que introduzca el usuario sera una cadena de texto
#Podemos convertirlo a un entero con la función int() age = int(age) o podemos pone antes del input int(input())
print(f"Hola {nombre}, tienes {age} años")

print("Obtener más de un valor a la vez")
country,city = input("En que pais y ciudad vives?").split() #La lista que vamos a conseguir, la vamos a separar en cada una de las variables

print(f"Vives en {country}, {city}")