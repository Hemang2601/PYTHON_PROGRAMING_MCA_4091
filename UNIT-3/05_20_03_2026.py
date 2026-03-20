class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def convertFahrenheit(self):
        result = (self.temp * 9/5) + 32
        print(f"{self.temp} C is equal to {result} F")
        return result

    def convertCelsius(self):
        result = (self.temp - 32) * 5/9
        print(f"{self.temp} F is equal to {result:.2f} C")
        return result



t1 = Temperature(int(input("Enter a temperature in Celsius : ")))
t1.convertFahrenheit()


t2 = Temperature(int(input("Enter a temperature in Farenhei : ")))
t2.convertCelsius()