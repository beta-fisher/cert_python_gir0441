'''
Autor: Angel Armando Ramirez Vazquez
Fecha: 4 sep 2022
'''
def is_prime(num):
    div = 2
    while div < num:
        if num % div == 0:
             return False
        div += 1
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()