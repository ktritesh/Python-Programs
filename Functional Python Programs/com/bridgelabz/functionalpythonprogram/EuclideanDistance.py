"""""
*author - Ritesh KT
*date - 28-07-2021
*time - 07:30 PM
*title - Euclidean distance
"""""
import math

class Distance:

    def userInput(self):
        #Taking input from user
        x2 = int(input("Enter the value of x2: "))
        y2 = int(input("Enter the value of y2: "))
        return x2, y2

    def euclideanDistance(self, x2, y2):
        #Euclidean distance Formula
        x1 = 0
        y1 = 0
        distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
        print("Euclidean distance is: ", distance)

#Main method
if __name__ == "__main__":
#Exception handling
    try:
        d = Distance()   #Creation object and d is the instance variable
        x2, y2 = d.userInput() #Calling method to input from user
        d.euclideanDistance(x2, y2) #Callling method to calculate euclidean distance
    except:
        print('Exception Occured')