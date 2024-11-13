class TemperatureConverter:
    def __init__(self, temp, unit):
        self.temp = temp
        self.unit = unit.lower()

    def to_celsius(self):
        """Converts Fahrenheit to Celsius"""
        celsius = (self.temp - 32) * 5 / 9
        return f"{self.temp}°F is {celsius:.2f}°C"

    def to_fahrenheit(self):
        """Converts Celsius to Fahrenheit"""
        fahrenheit = (self.temp * 9 / 5) + 32
        return f"{self.temp}°C is {fahrenheit:.2f}°F"

    def convert(self):
        """Determines which conversion to apply based on the unit"""
        if self.unit == "c":
            return self.to_fahrenheit()
        elif self.unit == "f":
            return self.to_celsius()
        else:
            return "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."

# Ask for temperature and unit from the user
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Create an instance of TemperatureConverter
converter = TemperatureConverter(temp, unit)

# Perform conversion and display the result
print(converter.convert())
input("")