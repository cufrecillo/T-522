# nombre = "Vito"
# apellido = "Genovese" # Designo apellido
# space = " "

# edad = 12
# is_adult = edad >= 18

# IF STATEMENTS:

# if edad >= 18:
#     print("Es adulto")
# else:
#     print("No es adulto")

# apellido_en_mayus = apellido.upper()
# print(apellido_en_mayus)
# edad.
# nombre_completo = "Vito Genoves"

# result = nombre_completo.replace("Genoves", "Fernández")
# print(result)

lorem = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of 'de Finibus Bonorum et Malorum' (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, 'Lorem ipsum dolor sit amet..'"

a = "hola"
b = "Hola"

# EJERCICIO 1:
# print(a.title()== b)
# print(a.capitalize() == b)
# print(a == b.lower())
# print(a.endswith("a") == b.endswith("a"))

# EJERCICIO 3:
# print(lorem.count("it") + lorem.count("It"))

# EJERCICIO 4:
# print(lorem.find("Ipsum"))
# print(lorem[34:39])

# EJERCICIO 5:
palabra = lorem.split(" ")
con_count = lorem.count(" ") + 1
# print("Con la función len: ", len(palabra))
# print("Con el método count: ", len(palabra))

# EJERCICIO 6:
limite_inferior = lorem.find("Richard")
resultado = lorem[limite_inferior: 171]
resultado = resultado.lower()
# print(resultado)

lista_palabras = lorem.split(" ") #Ejercicio 7
resultado = lista_palabras[30].lower()

# Explicación:
# ejemplo = "hola cómo estás?"
# print(ejemplo.find("h"))
# ejemplo = "Hola chau adi"
# print(ejemplo[5:9])
# ejemplo = "1"
# print(len(ejemplo))

# EJERCICIO 8
lista_palabras = lorem.split(" ")
# print(type(lista_palabras))
# print(lista_palabras[0])
# lista_ejemplo = [1, "una palabra", 3, 4, 5]
# print(lista_ejemplo[1])

password = "contraseña"
password = password.capitalize()