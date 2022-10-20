file = open("devices.txt", "r")
dispositivo = input("¿Qué dispositivo buscaba? \n")

for line in file:
    line = line.strip()
    if dispositivo in line:
        print(line)
    else:
       print("Dispositivo no encontrado")
file.close()