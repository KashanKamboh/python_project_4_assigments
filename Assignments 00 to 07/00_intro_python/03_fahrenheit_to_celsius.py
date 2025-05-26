def main():
    temprature = float(input("Enter the temprature in Fahrenheit:"))

    degrees_celsius = (temprature - 32) * 5.0/9.0


    print(f"Temrature:{temprature}F to {degrees_celsius}C")