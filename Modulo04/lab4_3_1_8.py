def isYearLeap(año):
    if año < 1582:
        return False
    elif año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

def daysInMonth(año, mes):
    MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(año) and mes == 2:
            return 29
    return MonthDays[mes-1]

def dayOfYear(año, mes, día):
    if año < 1582:
        return None
    if mes > 12 or mes < 1:
        return None
    if día > daysInMonth(año, mes) or día < 1:
        return None


    totalDays = día
    mes = mes - 1
    while mes > 0:
        totalDays += daysInMonth(año, mes)
        mes -= 1
    return totalDays

print(dayOfYear(2000, 12, 31))