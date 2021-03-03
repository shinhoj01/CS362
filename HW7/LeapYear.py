def leapyear(year):
    if year % 400 == 0:
        return "{} is a leap year".format(year)
    elif year % 100 == 0:
        return "{} is not a leap year".format(year)
    elif year % 4 == 0:
        return "{} is a leap year".format(year)
    else:
        return "{} is not a leap year".format(year)

year = int(input("Enter a year: "))
print(leapyear(year))
