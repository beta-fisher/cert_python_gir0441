file = open("devices.txt", "r")
dispositivo = []

for line in file:
    line = line.strip()
    dispositivo.appends(line)
print(dispositivo)
file.close()