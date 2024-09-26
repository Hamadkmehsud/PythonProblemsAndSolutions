def celsius_fahrenheit():
    celsius = float(input('Enter Celsius to convert into Fahrenheit: '))
    fahrenheit = (celsius*1.8) + 32
    print(f'{celsius} Celsius into fahrenheit are: {fahrenheit}')
celsius_fahrenheit()

def fahrenheit_celsius():
    fahrenheit = float(input('Enter Celsius to convert into Fahrenheit: '))
    celsius = (fahrenheit - 32) / 1.8
    print(f'{fahrenheit} fahrenheit into Celsius are: {celsius}')
fahrenheit_celsius()