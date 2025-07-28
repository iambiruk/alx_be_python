FAHRENHITE_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHITE_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHITE_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """Convert Celsiusi to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHITE_FACTOR) + 32
def main():
    try:
        temp_input = input("Enter the temprature to convert: ").strip()
        temprature = float(temp_input)
        unit = input("Is this temprature in Celsius or Fahrenheit? (C/F): ")
        if unit == 'F':
            celsius = convert_to_celsius(temprature)
            print(f"{temprature}°F is {celsius}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temprature)
            print(f"{temprature}°C is {fahrenheit}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for celsius or 'f' for Fahrenheit.")
    except ValueError:
        print("Invalid temprature. Please enter a numeric value.")
if __name__ == "__main__":
    main()
