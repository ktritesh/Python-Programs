"""""
*author - Ritesh KT
*date - 29-07-2021
*time - 09:00 AM
*title - WindChill
"""""

class WindChill:
    def __init__(self, temperature, speed):
        self.temperature = temperature      #Initialize constructor with parameters
        self.speed = speed                  #Initialize constructor with parameters

    def calculate(self):
        #define methods for calculate equation
        weatherService = 35.74+0.6215*self.temperature+(0.4275*self.
                          temperature-35.75)*pow(self.speed,0.16)
        return weatherService

while True:
    try:
        temperature = int(input("Enter the temperature less than 50 : "))
        if temperature < 0 or temperature > 50:
            print("Enter the valid temperature: ")
            break
        speed = int(input("Enter the speed more than 3 & less than 120 : "))
        if speed < 3 or speed > 120:
            print("Enter the valid speed")
            break
        windchill = WindChill(temperature, speed)  #Creating object of WindChill class
        nationalWeatherService = windchill.calculate() #take input from user and call the methods using object
        if nationalWeatherService == None:
            break
        print("National Weather Service : ", nationalWeatherService)
    except:
        print("Exception occured")