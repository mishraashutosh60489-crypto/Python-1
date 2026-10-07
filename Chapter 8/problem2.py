def temperature(celsius):
      farenheit = (celsius*9/5) + 32
      return farenheit
temp = float(input("Enter temperature in celsius : "))
f = temperature(temp)
print(f)
