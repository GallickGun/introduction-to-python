print("Temperature conversion")

celcius = float(input("Insert temperature in Celcius: "))
print('Room temp is: ', celcius, "Celcius")

reamur = (4/5) * celcius
print('Room temp is: ', reamur, "Reamur")

fahrenheit = ((4/5) * celcius) +32
print('Room temp is: ', fahrenheit, "Fahrenheit")

kelvin = celcius + 273
print('Room temp is: ', kelvin, "Kelvin")

fahrenheitInput = float(input("Insert temperature in Fahrenheit: "))
print("Room temp is: ", fahrenheitInput, "Fahrenheit")

fahrenheitToKelvin = (fahrenheitInput + 459.67) * 5/9
print('Room temp is: ', fahrenheitToKelvin, "Kelvin")

kelvinInput = float(input("Insert temperature in Kelvin: "))
print('Room temp is: ', kelvinInput, "Kelvin")

kelvinToFahrenheit = (kelvinInput - 273.15) * 9/5 + 32
print('Room temp is: ', kelvinToFahrenheit, "Fahrenheit")
