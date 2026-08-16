print("Engineering Unit Converter")
print("--------------------------")

print("1. Miles to Kilometers")
print("2. Feet to Meters")
print("3. Fahrenheit to Celsius")
print("4. PSI to kPa")

choice = input("Choose a conversion (1-4): ")

value = float(input("Enter the value: "))

if choice == "1":
    result = value * 1.60934
    print(f"{value} miles = {result:.2f} kilometers")

elif choice == "2":
    result = value * 0.3048
    print(f"{value} feet = {result:.2f} meters")

elif choice == "3":
    result = (value - 32) * 5 / 9
    print(f"{value}°F = {result:.2f}°C")

elif choice == "4":
    result = value * 6.89476
    print(f"{value} PSI = {result:.2f} kPa")

else:
    print("Invalid selection.")
