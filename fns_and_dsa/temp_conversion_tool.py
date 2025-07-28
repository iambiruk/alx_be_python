FAHRENHITE_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHITE_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHITE_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHITE_FACTOR) + 32
try:
     temp = float(input("Enter the temprature to convert: "))
        unit = input("Is this temprature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == 'C':
            result= convert_to_fahrenheit(temp)
            print(f"{temprature}°C is {result}°F")
        else:
            print("Invalid input, enter C or F")
except ValueError:
    print("Invalid temprature. Please enter a numeric value.")
