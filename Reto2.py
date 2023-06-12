# 1. El método count() retorna el número de veces que se repite un conjunto de caracteres especificado
nombre = "Jerome Amaya Amaya Sanabria"
print (nombre.count("Amaya"))

# 2. Los métodos find() e index() retornan la ubicación (comenzando desde el cero) en la que se encuentra el argumento indicado

print (nombre.find ("Sanabria"))
print (nombre.index ("Amaya"))

# Difieren en que esta última lanza ValueError cuando el argumento no es encontrado, mientras que aquélla retorna -1.

#print (nombre.find ("Perez"))
#print (nombre.index ("Paez"))

# 3. startswith() y endswith() indican si la cadena en cuestión comienza o termina con el conjunto de caracteres pasados como argumento, y retornan True o False en función de ello.

print(nombre.startswith("Jerome"))
print(nombre.endswith("Jerome"))
# 4. Ambos métodos son preferidos ante la opción de emplear slicing.
print (nombre [6]=="Jerome")

# 5. Los métodos isdigit(), isnumeric() e isdecimal() determinan si todos los caracteres de la cadena son dígitos, números o números decimales.
digito = "1234"
cadena = "diccionario"
print(digito.isnumeric())
print(cadena.isdecimal())
print(cadena.isdigit())

# Determina si todos los caracteres son alfanuméricos.
print("abc123".isalnum())
print("123".isalnum())

# Determina si todos los caracteres son alfabéticos.
print("abcdef".isalpha())
print("abc123".isalpha())

# Determina si todas las letras son minúsculas.
print("abcdef".islower())
print ("ABCDEF".islower())
# Mayúsculas.
print ("ABCDEF".isupper())
print ("ABCDEc".isupper())

# Determina si la cadena contiene todos caracteres imprimibles.
print("Hola \t mundo!".isprintable())

# Determina si la cadena contiene solo espacios.
print("Hola mundo".isspace())
print("    ".isspace())

# capitalize() retorna la cadena con su primera letra en mayúscula.
print ("hola".capitalize())

# encode() codifica la cadena con el mapa de caracteres especificado y retorna una instancia del tipo bytes.

print ("hola".encode("utf-8"))
# Los métodos center(), ljust() y rjust() alinean una cadena en el centro, la izquierda o la derecha respectivamente. 
# Toman un argumento, la cantidad de caracteres respecto de la cual se producirá la alineación.
print("Jerome".center(10))
print("Jerome".ljust(10))
print("Jerome".rjust(10))

# lower() y upper() retornan una copia de la cadena con todas sus letras en minúsculas o mayúsculas según corresponda.
print("ESTO es una prueba".lower())
print("ESTO es una prueba".upper())

# swapcase(), por su parte, cambia las mayúsculas por minúsculas y viceversa.

print("ESTO es una prueba".swapcase())

# Las funciones strip(), lstrip() y rstrip() remueven los espacios en blanco que preceden y/o suceden a la cadena.

s = " Hola mundo! "
s.strip()

'Hola mundo!'
# Remueve los de la derecha.
s.rstrip()
' Hola mundo!'
# Remueve los de la izquierda.
s.lstrip()
'Hola mundo! '
# replace() ─ampliamente utilizado─ reemplaza una cadena por otra
nom = "Felipe"
print(nom.replace("Felipe","Andres"))
# split(), cuyo separador por defecto son espacios en blanco y saltos de línea.
print("Esto es una prueba \n ESTO ES UNA PRUEBA".split())
print("Esto es una prueba \n ESTO ES UNA PRUEBA".splitlines())

# artition(), que retorna una tupla de tres elementos:
# el bloque de caracteres anterior a la primera ocurrencia del separador, el separador mismo, y el bloque posterior.
s = "Realizar esta Prueba. Ahora"
print(s.partition(" "))
print(s.rpartition(" "))

# join() ─sumamente útil─, que debe ser llamado desde una cadena
# que actúa como separador para unir dentro de una misma cadena resultante los elementos de una lista.
lista = ["juan","pedro","luis","daniel","dario","lucas"]
print(lista)
print(",".join(lista) )

# Concatena una tupla de strings con: " y "

print( " y ".join(["A","B","C","D"]))