def devorador(entrada):
    entrada = entrada.upper()
    
    for letra in entrada:
        if letra == "A" or letra=="E" or letra =="I" or letra =="O" or letra =="U":
            continue
        else:
            print(letra, end=' ')

entrada = input("Ingrese la palabra: ")
devorador(entrada)
