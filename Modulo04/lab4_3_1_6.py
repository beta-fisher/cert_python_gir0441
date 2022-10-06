
def is_year_leap(year):
    Bisiesto = False
    diviEntre_4 = year % 4
    diviEntre_100 = year % 100
    diviEntre_400 = year % 400

    if year >= 1582:
        if diviEntre_4 != 0:
            Bisiesto = False
        elif diviEntre_100 != 0:
            Bisiesto = True
        elif diviEntre_400 != 0:
            Bisiesto = False
        else:
            Bisiesto = True
    else:
        Bisiesto = False

    return Bisiesto

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
