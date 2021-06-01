test = ["Juan","Vito","Vicente","Renzo", "Joaquin"]

# test.append("Poncio")
# test.append("Andrés")

count = 0
user = input("Busca: ")
while count < len(test):
    if user == test[count]:
        print(count)
    else:
        print("El user no está")
    count += 1

