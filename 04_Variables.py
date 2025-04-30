###
#Curso de python desde 0, primero empecezamos con un Hola mundo
# #04 - Variables
# las variables sirven para guardar datos en memoria
# python es un lenguaje de tipado dinamico y de tipado fuerte
###

#Asignar una vaviable
#Solo hace falta escribir...
nombre = "Vocra"
edad = 19

print(nombre)

print(edad)
#Podemos cambiar el valor de la variable
edad = 20
print(edad)

#Tipado Dinamico: El tipo de dato se determina en tiempo de ejecución
#No tienes que declararlo explicitamente como en c++

#Podemos cambiar el tipo de dato de la variable
#nombre = 19
#print(nombre) #Ahora es un entero

# Tipado fuerte: Python no realiza conversiones de tipo automaticas
# Si queremos mostrar una evalución de algun dato podemos:
# Cadenas literales formateadas (f string)

#f-string (literal de cadena de formato)
print(f"Hola {nombre} tengo {edad- 2} años") 

#Convenciones de nombres de variables
mi_nombre_de_variable = "Vocra" #snake_case |Es el guión bajo lo que separa las palabras 
#miNombreDeVariable = "Vocra" #camelCase | La primera letra de cada palabra es mayúscula
#MiNombreDeVariable = "Vocra" #PascalCase | La primera letra de cada palabra es mayúscula

#Python no tiene constantes 💀
MI_CONSTANTE = 3.14 #UPPER_CASE -> Constantes

#Se puede hacer lo siguiente con las variables:
is_user_logged_in:bool = True #Especificar el tipo de dato de la variable
#Se podria decfir que :bool es un comentario que nos dice de que tipo es
print (is_user_logged_in) #True
#Se le puede cambiar la configuración en el editor, aunque a python se la pela
#Esto de los :bool afecta a aquellas variables que hayan sido declaradas anteriormente e incluso cambiadas

#Lo malo esque lo siguiente funciona:
is_user_logged_in = 10 #Es un entero
print (is_user_logged_in) #10