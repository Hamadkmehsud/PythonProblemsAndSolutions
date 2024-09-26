def leap_year():
    year = int(input('Enter a year to check if its a Leap Year: '))

    if (year % 4 == 0 and year % 100 != 0) or  year % 400 == 0:
        print(f'{year} is a Leap Year')
    else:
        print(f'{year} is a NOT a Leap Year')

leap_year()