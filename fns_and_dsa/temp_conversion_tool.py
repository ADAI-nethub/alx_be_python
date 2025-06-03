# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_OFFSET = 32

def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor"""
    celsius = (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            print("Error: Please enter either 'C' or 'F' for the temperature unit.")
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()