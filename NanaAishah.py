temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 0:
    print("Freezing cold")
elif temperature <= 15:
    print("Cold")
elif temperature <= 25:
    print("Cool")
elif temperature <= 35:
    print("Warm")
else:
    print("Hot")