file = open("devices.txt", "a")
while True:
    newItem = input("Dispositivo para agregar: ")
    if newItem == "exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()