import datetime

def month_str(month_integer):
    if month_integer == 1:
        return 'Janeiro'
    elif month_integer == 2:
        return 'Fevereiro'
    elif month_integer == 3:
        return 'Março'
    elif month_integer == 4:
        return 'Abril'
    elif month_integer == 5:
        return 'Maio'
    elif month_integer == 6:
        return 'Junho'
    elif month_integer == 7:
        return 'Julho'
    elif month_integer == 8:
        return 'Agosto'
    elif month_integer == 9:
        return 'Setembro'
    elif month_integer == 10:
        return 'Outubro'
    elif month_integer == 11:
        return 'Novembro'
    elif month_integer == 12:
        return 'Dezembro'

def get_date_as_str():
    today = datetime.datetime.now()
    return str(today.day) + ' de ' + month_str(today.month) + ' de ' + str(today.year)