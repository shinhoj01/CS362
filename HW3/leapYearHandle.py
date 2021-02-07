def checkLeap(year):
    # Check if input is numeric
    if (year.isnumeric()):
        # Convert input to integer
        year = int(year)

        # Check if input is leap year
        if (year % 400) == 0:
            print("{} is a leap year".format(year))
        elif (year % 100) == 0:
            print("{} is not a leap year".format(year))
        elif (year % 4) == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is not valid input".format(year))

year = input("Enter a year: ")
checkLeap(year)
input("Press Enter to exit...")
