def calculate(celsius) :
    farenheit = (celsius * 9/5) + 32
    print(format(farenheit, ".2f"))

calculate(int(input("Enter Celsius: ")))