def is_leap(year):
    leap = False

    divisible_four = year % 4
    divisible_cem = year % 100
    divisible_quatrocentos = year % 400

    eleva_quinta = year ** 5

    if 1900 <= year <= eleva_quinta:
        if(divisible_quatrocentos == 0) or (divisible_four == 0 and divisible_cem != 0):
            return True
        else:
            return False
    else:
        print('ano invalido')
    return leap

year = int(input())
print(is_leap(year))

